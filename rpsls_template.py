#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ������İ�̷���
���ڣ�2019.11.14
"""

import random
comp_number=random.randrange(0,5)

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(comp_number):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if comp_number==0:
        print("�������ѡ��Ϊʯͷ")
        return
    elif comp_number==1:
        print("�������ѡ��Ϊʷ����")
        return
    elif comp_number==2:
        print("�������ѡ��Ϊֽ")
        return
    elif comp_number==3:
        print("�������ѡ��Ϊ����")
        return
    elif comp_number==4:
        print("�������ѡ��Ϊ����")
        return    
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


#��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number=="ʯͷ":
        print("����ѡ��Ϊʯͷ")
        number=0
        return number
    elif number=="ʷ����":
        print("����ѡ��Ϊʷ����")
        number=1
        return number
    elif number=="ֽ":
        print("����ѡ��Ϊֽ")
        number=2
        return number
    elif number=="����":
        print("����ѡ��Ϊ����")
        number=3
        return number
    elif number=="����":
        print("����ѡ��Ϊ����")
        number=4
        return number 
    else:
        number=5
        return number
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

  #��дִ�д���,������ɺ�passɾ��


def rpsls(choice_name):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    a=number_to_name(choice_name)
    name_to_number(comp_number)
    b=comp_number
    if a==b:
        print("���ͼ��������һ����")
    elif a==5:
        print("Error: No Correct Name")
        return      
    elif a==0 and b==4:
        print("��Ӯ��")
    elif a==0 and b==3:
        print("��Ӯ��")
    elif a==1 and b==0:
        print("��Ӯ��")
    elif a==1 and b==4:
        print("��Ӯ��")
    elif a==2 and b==0:
        print("��Ӯ��")
    elif a==2 and b==1:
        print("��Ӯ��")
    elif a==3 and b==2:
        print("��Ӯ��")
    elif a==3 and b==1:
        print("��Ӯ��")
    elif a==4 and b==2:
        print("��Ӯ��")
    elif a==4 and b==3:
        print("��Ӯ��")
    else:
        print("�����Ӯ��")
    return
    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

     #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


