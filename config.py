# 従業員情報の追加
emp_info = {}
emp_info["model_1"] = "00001"
emp_info["model_2"] = "00002"
emp_info["model_3"] = "00003"
emp_info["model_4"] = "00004"

# パスワード認証モード（1: オン, 0: オフ）
mode = 1

# 顔を識別する閾値の設定
# 下記の数値より少なくすると顔が本人でも別の人と識別してしまうため、下記の値が丁度良い
threshold = 0.5