# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Version: 2.9.1
# https://stefanoflore.it
# https://ai-wiz.art

import os
import random

script_dir = os.path.dirname(__file__)

# read txt file

def pmReadTxt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        values = [line.strip() for line in lines]
        return values

# Apply weight
    
def applyWeight(text, weight):
    if weight == 1:
        return text
    else:
        return f"({text}:{round(weight,2)})"

# setup vars

shot_list = pmReadTxt(os.path.join(script_dir, "lists/shot_list.txt"))
shot_list.sort()
shot_list = ['-'] + shot_list

gender_list = pmReadTxt(os.path.join(script_dir, "lists/gender_list.txt"))
gender_list.sort()
gender_list = ['-'] + gender_list

face_shape_list = pmReadTxt(os.path.join(script_dir, "lists/face_shape_list.txt"))
face_shape_list.sort()
face_shape_list = ['-'] + face_shape_list

facial_expressions_list = pmReadTxt(os.path.join(script_dir, "lists/face_expression_list.txt"))
facial_expressions_list.sort()
facial_expressions_list = ['-'] + facial_expressions_list

nationality_list = pmReadTxt(os.path.join(script_dir, "lists/nationality_list.txt"))
nationality_list.sort()
nationality_list = ['-'] + nationality_list

hair_style_list = pmReadTxt(os.path.join(script_dir, "lists/hair_style_list.txt"))
hair_style_list.sort()
hair_style_list = ['-'] + hair_style_list

light_type_list = pmReadTxt(os.path.join(script_dir, "lists/light_type_list.txt"))
light_type_list.sort()
light_type_list = ['-'] + light_type_list

light_direction_list = pmReadTxt(os.path.join(script_dir, "lists/light_direction_list.txt"))
light_direction_list.sort()
light_direction_list = ['-'] + light_direction_list

eyes_color_list = pmReadTxt(os.path.join(script_dir, "lists/eyes_color_list.txt"))
eyes_color_list.sort()
eyes_color_list = ['-'] + eyes_color_list

eyes_shape_list = pmReadTxt(os.path.join(script_dir, "lists/eyes_shape_list.txt"))
eyes_shape_list.sort()
eyes_shape_list = ['-'] + eyes_shape_list

hair_color_list = pmReadTxt(os.path.join(script_dir, "lists/hair_color_list.txt"))
hair_color_list.sort()
hair_color_list = ['-'] + hair_color_list

hair_length_list = pmReadTxt(os.path.join(script_dir, "lists/hair_length_list.txt"))
hair_length_list.sort()
hair_length_list = ['-'] + hair_length_list

body_type_list = pmReadTxt(os.path.join(script_dir, "lists/body_type_list.txt"))
body_type_list.sort()
body_type_list = ['-'] + body_type_list

beard_list = pmReadTxt(os.path.join(script_dir, "lists/beard_list.txt"))
beard_list.sort()
beard_list = ['-'] + beard_list

model_pose_list = pmReadTxt(os.path.join(script_dir, "lists/model_pose_list.txt"))
model_pose_list.sort()
model_pose_list = ['-'] + model_pose_list

style_1_list = pmReadTxt(os.path.join(script_dir, "lists/style_list.txt"))
style_1_list.sort()
style_1_list = ['-'] + style_1_list

style_2_list = pmReadTxt(os.path.join(script_dir, "lists/style_list.txt"))
style_2_list.sort()
style_2_list = ['-'] + style_2_list

lips_shape_list = pmReadTxt(os.path.join(script_dir, "lists/lips_shape_list.txt"))
lips_shape_list.sort()
lips_shape_list = ['-'] + lips_shape_list

lips_color_list = pmReadTxt(os.path.join(script_dir, "lists/lips_color_list.txt"))
lips_color_list.sort()
lips_color_list = ['-'] + lips_color_list

makeup_list = pmReadTxt(os.path.join(script_dir, "lists/makeup_list.txt"))
makeup_list.sort()
makeup_list = ['-'] + makeup_list

clothes_list = pmReadTxt(os.path.join(script_dir, "lists/clothes_list.txt"))
clothes_list.sort()
clothes_list = ['-'] + clothes_list

class PortraitMaster:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 1.95
        return {
            "optional": {
                "种子": ("INT", {"forceInput": False}),
            },
            "required": {
                "肖像类型": (shot_list, {
                    "default": shot_list[0],
                }),
                "肖像类型权重": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "性别": (gender_list, {
                    "default": gender_list[0],
                }),
                "中性化": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "年龄": ("INT", {
                    "default": 30,
                    "min": 18,
                    "max": 90,
                    "step": 1,
                    "display": "slider",
                }),
                "国籍1": (nationality_list, {
                    "default": nationality_list[0],
                }),
                "国籍2": (nationality_list, {
                    "default": nationality_list[0],
                }),
                "国籍混合比例": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": 1,
                    "step": 0.05,
                    "display": "slider",
                }),
                "体型": (body_type_list, {
                    "default": body_type_list[0],
                }),
                "体型权重": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "姿势": (model_pose_list, {
                    "default": model_pose_list[0],
                }),
                "衣服": (clothes_list, {
                    "default": clothes_list[0],
                }),

                "眼睛颜色": (eyes_color_list, {
                    "default": eyes_color_list[0],
                }),
                "眼睛形状": (eyes_shape_list, {
                    "default": eyes_shape_list[0],
                }),
                "唇色": (lips_color_list, {
                    "default": lips_color_list[0],
                }),
                "唇形": (lips_shape_list, {
                    "default": lips_shape_list[0],
                }),
                "面部表情": (facial_expressions_list, {
                    "default": facial_expressions_list[0],
                }),
                "面部表情权重": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "脸型": (face_shape_list, {
                    "default": face_shape_list[0],
                }),
                "脸型权重": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "面部不对称性": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "发型": (hair_style_list, {
                    "default": hair_style_list[0],
                }),
                "发色": (hair_color_list, {
                    "default": hair_color_list[0],
                }),
                "发长": (hair_length_list, {
                    "default": hair_length_list[0],
                }),
                "凌乱化": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "妆造": (makeup_list, {
                    "default": makeup_list[0],
                }),
                "胡须": (beard_list, {
                    "default": beard_list[0],
                }),
                "自然皮肤": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "素颜": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "清洁的脸": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "干燥的脸": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤细节度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤毛孔": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "酒窝": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皱纹": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "雀斑": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "痣": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤瑕疵度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤痤疮": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "深肤色": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "眼睛细节度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "虹膜细节度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "圆形虹膜": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "圆形瞳孔": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "光照类型": (light_type_list, {
                    "default": light_type_list[0],
                }),
                "光源方向": (light_direction_list, {
                    "default": light_direction_list[0],
                }),
                "光照强度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "写实化": (["enable", "disable"],),
                "起始提示词": ("STRING", {
                    "multiline": True,
                    "default": "raw photo, (realistic:1.5)"
                }),
                "附加提示词": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "结尾提示词": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "反向提示词": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "风格1": (style_1_list, {
                    "default": style_1_list[0],
                }),
                "风格1权重": ("FLOAT", {
                    "default": 1.5,
                    "min": 1,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "风格2": (style_2_list, {
                    "default": style_2_list[0],
                }),
                "风格2权重": ("FLOAT", {
                    "default": 1.5,
                    "min": 1,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "随机肖像类型": ("BOOLEAN", {"default": False}),
                "随机性别": ("BOOLEAN", {"default": False}),
                "随机年龄": ("BOOLEAN", {"default": False}),
                "随机中性化": ("BOOLEAN", {"default": False}),
                "随机国籍": ("BOOLEAN", {"default": False}),
                "随机体型": ("BOOLEAN", {"default": False}),
                "随机姿势": ("BOOLEAN", {"default": False}),
                "随机衣服": ("BOOLEAN", {"default": False}),
                "随机眼睛颜色": ("BOOLEAN", {"default": False}),
                "随机眼睛形状": ("BOOLEAN", {"default": False}),
                "随机唇色": ("BOOLEAN", {"default": False}),
                "随机唇形": ("BOOLEAN", {"default": False}),
                "随机表情": ("BOOLEAN", {"default": False}),
                "随机脸型": ("BOOLEAN", {"default": False}),
                "随机发型": ("BOOLEAN", {"default": False}),
                "随机发色": ("BOOLEAN", {"default": False}),
                "随机发长": ("BOOLEAN", {"default": False}),
                "随机凌乱化": ("BOOLEAN", {"default": False}),
                "随机妆造": ("BOOLEAN", {"default": False}),
                "随机雀斑": ("BOOLEAN", {"default": False}),
                "随机痣": ("BOOLEAN", {"default": False}),
                "随机皮肤瑕疵": ("BOOLEAN", {"default": False}),
                "随机胡须": ("BOOLEAN", {"default": False}),
                "随机风格1": ("BOOLEAN", {"default": False}),
                "随机风格2": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("positive", "negative",)

    FUNCTION = "pm"

    CATEGORY = "AI WizArt"

    def pm(self, 肖像类型="-", 肖像类型权重=1, 性别="-", 体型="-", 体型权重=0, 眼睛颜色="-", 面部表情="-", 面部表情权重=0, 脸型="-", 脸型权重=0, 国籍1="-", 国籍2="-", 国籍混合比例=0.5, 年龄=30, 发型="-", 发色="-", 凌乱化=0, 酒窝=0, 雀斑=0, 皮肤毛孔=0, 皮肤细节度=0, 痣=0, 皮肤瑕疵度=0, 皱纹=0, 深肤色=0, 眼睛细节度=1, 虹膜细节度=1, 圆形虹膜=1, 圆形瞳孔=1, 面部不对称性=0, 附加提示词="", 起始提示词="", 结尾提示词="", 光照类型="-", 光源方向="-", 光照强度=0, 反向提示词="", 写实化="disable", 胡须="-", 姿势="-", 皮肤痤疮=0, 风格1="-", 风格1权重=0, 风格2="-", 风格2权重=0, 中性化=0, 自然皮肤=0, 素颜=0, 清洁的脸=0, 干燥的脸=0, 发长="-", 眼睛形状="-", 唇色="-", 唇形="-", 妆造="-", 衣服="-", 种子=0, 随机肖像类型=False, 随机性别=False, 随机年龄=False, 随机中性化=False, 随机国籍=False, 随机体型=False, 随机姿势=False, 随机衣服=False, 随机眼睛颜色=False, 随机眼睛形状=False, 随机唇色=False, 随机唇形=False, 随机表情=False, 随机脸型=False, 随机发型=False, 随机发色=False, 随机发长=False, 随机凌乱化=False, 随机妆造=False, 随机雀斑=False, 随机痣=False, 随机皮肤瑕疵=False, 随机胡须=False, 随机风格1=False, 随机风格2=False):

        prompt = []

        # RANDOMIZER SWITCHES

        
        if 随机肖像类型:
            肖像类型 = random.choice(shot_list)
            肖像类型权重 = random.uniform(0.5,1.25)

        if 随机性别:
            性别 = random.choice(gender_list)

        if 随机年龄:
            年龄 = random.randint(18,75)

        if 随机国籍:
            国籍1 = random.choice(nationality_list)
            国籍2 = "-"

        if 随机发型:
            发型 = random.choice(hair_style_list)

        if 随机姿势:
            姿势 = random.choice(model_pose_list)

        if 随机眼睛颜色:
            眼睛颜色 = random.choice(eyes_color_list)

        if 随机眼睛形状:
            眼睛形状 = random.choice(eyes_shape_list)

        if 随机唇色:
            唇色 = random.choice(lips_color_list)

        if 随机唇形:
            唇形 = random.choice(lips_shape_list)

        if 随机发色:
            发色 = random.choice(hair_color_list)

        if 随机发长:
            发长 = random.choice(hair_length_list)

        if 随机表情:
            面部表情 = random.choice(facial_expressions_list)
            面部表情权重 = random.uniform(0.5,1.25)

        if 随机脸型:
            脸型 = random.choice(face_shape_list)
            脸型权重 = random.uniform(0.5,1.25)

        if 随机体型:
            体型 = random.choice(body_type_list)
            体型权重 = random.uniform(0.25,1.25)

        if 随机胡须:
            胡须 = random.choice(beard_list)

        if 随机中性化:
            中性化 = random.uniform(0,1)

        if 随机凌乱化:
            凌乱化 = random.uniform(0,1.35)

        if 随机衣服:
            衣服 = random.choice(clothes_list)

        if 随机妆造:
            妆造 = random.choice(makeup_list)

        if 随机雀斑:
            雀斑 = random.uniform(0,1.35)

        if 随机痣:
            痣 = random.uniform(0,1.35)

        if 随机风格1:
            风格1 = random.choice(style_1_list)
            风格1权重 = random.uniform(0.5,1.5)

        if 随机风格2:
            风格2 = random.choice(style_2_list)
            风格2权重 = random.uniform(0.5,1.5)

        if 随机皮肤瑕疵:
            皮肤瑕疵度 = random.uniform(0.15,1)

        # OPTIONS

        if 性别 == "-":
            性别 = ""
        else:
            性别 = 性别 + " "

        if 国籍1 != '-' and 国籍2 != '-':
            nationality = f"[{国籍1}:{国籍2}:{round(国籍混合比例, 2)}] "
        elif 国籍1 != '-':
            nationality = 国籍1 + " "
        elif 国籍2 != '-':
            nationality = 国籍2 + " "
        else:
            nationality = ""

        if 起始提示词 != "":
            prompt.append(f"{起始提示词}")

        if 肖像类型 != "-" and 肖像类型权重 > 0:
            prompt.append(applyWeight(肖像类型,肖像类型权重))

        prompt.append(f"({nationality}{性别}{round(年龄)}-years-old:1.5)")

        if 中性化 > 0:
            prompt.append(applyWeight('中性化',中性化))

        if 体型 != "-" and 体型权重 > 0:
            prompt.append(applyWeight(f"{体型}, {体型} body",体型权重))

        if 姿势 != "-":
            prompt.append(f"({姿势}:1.25)")

        if 衣服 != "-":
            prompt.append(f"({衣服}:1.05)")

        if 眼睛颜色 != "-":
            prompt.append(f"({眼睛颜色} eyes:1.05)")

        if 眼睛形状 != "-":
            prompt.append(f"({眼睛形状}:1.05)")

        if 唇色 != "-":
            prompt.append(f"({唇色}:1.05)")

        if 唇形 != "-":
            prompt.append(f"({唇形}:1.05)")

        if 妆造 != "-":
            prompt.append(f"({妆造}:1.05)")

        if 面部表情 != "-" and 面部表情权重 > 0:
            prompt.append(applyWeight(f"{面部表情}, {面部表情} expression",面部表情权重))

        if 脸型 != "-" and 脸型权重 > 0:
            prompt.append(applyWeight(f"{脸型} shape face",脸型权重))

        if 发型 != "-":
            prompt.append(f"({发型} cut hairstyle:1.05)")

        if 发色 != "-":
            prompt.append(f"({发色} hair:1.05)")

        if 发长 != "-":
            prompt.append(f"({发长}:1.05)")

        if 胡须 != "-":
            prompt.append(f"({胡须}:1.15)")

        if 凌乱化 != "-" and 凌乱化 > 0:
            prompt.append(applyWeight('凌乱化',凌乱化))

        if 附加提示词 != "":
            prompt.append(f"{附加提示词}")

        if 自然皮肤 > 0:
            prompt.append(applyWeight('natural skin',自然皮肤))

        if 素颜 > 0:
            prompt.append(applyWeight('bare face',素颜))

        if 清洁的脸 > 0:
            prompt.append(applyWeight('washed-face',清洁的脸))

        if 干燥的脸 > 0:
            prompt.append(applyWeight('dried-face',干燥的脸))

        if 皮肤细节度 > 0:
            prompt.append(applyWeight('skin details, skin texture',皮肤细节度))

        if 皮肤毛孔 > 0:
            prompt.append(applyWeight('skin pores',皮肤毛孔))

        if 皮肤瑕疵度 > 0:
            prompt.append(applyWeight('skin imperfections',皮肤瑕疵度))

        if 皮肤痤疮 > 0:
            prompt.append(applyWeight('acne, skin with acne',皮肤痤疮))

        if 皱纹 > 0:
            prompt.append(applyWeight('皱纹',皱纹))

        if 深肤色 > 0:
            prompt.append(applyWeight('tanned skin',深肤色))

        if 酒窝 > 0:
            prompt.append(applyWeight('酒窝',酒窝))

        if 雀斑 > 0:
            prompt.append(applyWeight('雀斑',雀斑))

        if 痣 > 0:
            prompt.append(applyWeight('痣',痣))

        if 眼睛细节度 > 0:
            prompt.append(applyWeight('eyes details',眼睛细节度))

        if 虹膜细节度 > 0:
            prompt.append(applyWeight('iris details',虹膜细节度))

        if 圆形虹膜 > 0:
            prompt.append(applyWeight('circular details',圆形虹膜))

        if 圆形瞳孔 > 0:
            prompt.append(applyWeight('circular pupil',圆形瞳孔))

        if 面部不对称性 > 0:
            prompt.append(applyWeight('facial asymmetry, face asymmetry',面部不对称性))

        if 光照类型 != '-' and 光照强度 > 0:
            if 光源方向 != '-':
                prompt.append(applyWeight(f"{光照类型} {光源方向}",光照强度))
            else:
                prompt.append(applyWeight(f"{光照类型}",光照强度))

        if 风格1 != '-' and 风格1权重 > 0:
            prompt.append(applyWeight(风格1,风格1权重))

        if 风格2 != '-' and 风格2权重 > 0:
            prompt.append(applyWeight(风格2,风格2权重))

        if 结尾提示词 != "":
            prompt.append(f"{结尾提示词}")

        prompt = ", ".join(prompt)
        prompt = prompt.lower()

        if 写实化 == "enable":
            prompt = prompt + ", (professional photo, balanced photo, balanced exposure:1.2)"

        if 写实化 == "enable":
            反向提示词 = 反向提示词 + ", (shinny skin, shiny skin, reflections on the skin, skin reflections:1.35)"

        print("=============================================================")
        print("Portrait Master positive prompt:")
        print(prompt)
        print("")
        print("Portrait Master negative prompt:")
        print(反向提示词)
        print("=============================================================")

        return (prompt,反向提示词,)
    
NODE_CLASS_MAPPINGS = {
    "PortraitMaster": PortraitMaster
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PortraitMaster": "Portrait Master v.2.9"
}
