from gradio_client import Client

def extract_model_parameters(space_name, hf_token=None):
    """
    Hugging Face Spaceからパラメータ情報を抽出し、ComfyUI用の辞書形式で返す
    
    Args:
        space_name (str): HF Spaceの名前 (例: "black-forest-labs/FLUX.1-dev")
        hf_token (str, optional): HF認証トークン
    
    Returns:
        dict: {
            'api_name': str,
            'parameters': {
                'param_name': {
                    'type': str,  # 'str', 'float', 'int', 'bool'
                    'required': bool,
                    'default': any,
                    'description': str
                }
            }
        }
    """
    try:
        # クライアント作成
        if hf_token:
            client = Client(space_name, hf_token=hf_token)
        else:
            client = Client(space_name)
        
        # API情報を辞書形式で取得
        api_info = client.view_api(return_format="dict")
        
        # 最初のエンドポイントを取得
        if not api_info or 'named_endpoints' not in api_info:
            return {'api_name': None, 'parameters': {}}
        
        endpoints = api_info['named_endpoints']
        if not endpoints:
            return {'api_name': None, 'parameters': {}}
        
        # 最初のエンドポイントを使用
        endpoint = list(endpoints.values())[0]
        api_name = endpoint.get('api_name', '/predict')
        
        parameters = {}
        
        # パラメータ情報を解析
        for param_info in endpoint.get('parameters', []):
            param_name = param_info.get('parameter_name', '')
            data_type = param_info.get('parameter_type', 'str')
            required = param_info.get('parameter_has_default', True) == False
            default_value = param_info.get('parameter_default', None)
            ui_type = param_info.get('component', 'Unknown')
            
            # データ型をPython型に変換
            if 'str' in data_type:
                py_type = 'str'
            elif 'float' in data_type or 'number' in data_type:
                py_type = 'float'
            elif 'int' in data_type:
                py_type = 'int'
            elif 'bool' in data_type:
                py_type = 'bool'
            else:
                py_type = 'str'  # デフォルト
            
            # デフォルト値の型変換
            if default_value is not None:
                if py_type == 'bool':
                    default_value = bool(default_value)
                elif py_type == 'float':
                    try:
                        default_value = float(default_value)
                    except:
                        default_value = 0.0
                elif py_type == 'int':
                    try:
                        default_value = int(default_value)
                    except:
                        default_value = 0
            
            # requiredでdefault_valueがNoneの場合、適当な値を設定
            if required and default_value is None:
                if py_type == 'str':
                    if 'prompt' in param_name.lower():
                        default_value = "a beautiful landscape"
                    else:
                        default_value = ""
                elif py_type == 'float':
                    default_value = 1.0
                elif py_type == 'int':
                    default_value = 1
                elif py_type == 'bool':
                    default_value = True
            
            parameters[param_name] = {
                'type': py_type,
                'required': required,
                'default': default_value,
                'ui_type': ui_type,
                'description': param_info.get('parameter_description', '')
            }
        
        return {
            'api_name': api_name,
            'parameters': parameters
        }
        
    except Exception as e:
        print(f"エラー: {e}")
        return {'api_name': None, 'parameters': {}}

# テスト実行
if __name__ == "__main__":
    # テスト用のspace (実際のFLUX.1-devに置き換え)
    space_name = "black-forest-labs/FLUX.1-dev"  # または他のspace
    
    print(f"=== {space_name} のパラメータ抽出 ===")
    result = extract_model_parameters(space_name)
    
    print(f"API名: {result['api_name']}")
    print("パラメータ:")
    for param_name, param_info in result['parameters'].items():
        print(f"  {param_name}:")
        print(f"    型: {param_info['type']}")
        print(f"    必須: {param_info['required']}")
        print(f"    デフォルト: {param_info['default']}")
        print(f"    UI型: {param_info['ui_type']}")
        print()