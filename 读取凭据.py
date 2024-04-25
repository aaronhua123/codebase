# import win32cred
#
# # 检索Windows凭据
# cred = win32cred.CredRead('MicrosoftAccount:user=cjhdwyyx@163.com', win32cred.CRED_TYPE_GENERIC, 0)
#
# # 获取凭据属性
# username = cred['UserName']
# password = cred['CredentialBlob']
# print(cred)