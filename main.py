
# თქვენი მიზანია მოცელული დიქტის ველიუები გახდეს
#  ქიები ხოლო ქიები პირიქით ველიუები.
#  # მაგალითად "Programing" უნდა შეესაბამებოდეს ყველა ის
# მოსწავლე რომელიც გადის ამ საგანს. # შედეგი უნდა იყოს მსგავსი:
#
#
# dct1 = {
#     "David": ["Programing", "Calculus", "Algorithms"],
#     "John": ["Calculus", "OOP", "Data Bases"],
#     "George": ["Web development", "Data Bases", "Calculus", "Algorithms"],
#     "Steve": ["Linux"]
# }
#
# result_dict = {}
#
# for key, value in dct1.items():
#     if isinstance(value, str):
#         kay = [value]
#
#     for kay in value :
#         if kay not in result_dict:
#             result_dict[kay] = []
#         result_dict[kay].append(key)
#
# print(result_dict)
#



# leqtoris dawerili
# result_dict = {}
# for key, value in dct1.items():
#     # print(value)
#     if isinstance(value, str) or type(value) == str:
#         result_dict[value] = key
#         continue
#     # print(item, key)
#     for subject in value:
#         if subject not in result_dict:
#             result_dict[subject] = []
#         result_dict[subject].append(key)
#     # print(subject)
# print(result_dict)












