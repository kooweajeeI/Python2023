# %% [markdown]
# # 주피터 노트북 사용법 학습
# 
# ## 마크다운, 파이썬 셀을 추가
# - 현재 셀 앞에 셀 추가 : a
# - 현재 셀 뒤에 셀 추가 : b
# - 코드 셀 -> 마크다운으로 변경 : 포커스만 있는 (커서 깜빡임 없는) 상태에서 m
# - 마크다운 -> 코드 셀 : 포커스 상태 y

# %%
# 최초 작성된 Python 셀

# %% [markdown]
# ## 파이썬 셀 실행
# - Ctrl + Enter : 입력 셀 실행
# 
# - Shift + Enter : 입력 셀 실행 후 아래 셀로 이동 (없으면 새로운 셀 추가)
# 
# - Alt + Enter : 입력영역 실행 후 아래 새로운 영역 추가
# 
# - Ctrl + / 또는 Ctrl + K,C : 주석처리

# %%
print('Hello, Jupyter')

# %% [markdown]
# ## 디버깅
# 아무리 강조해도 지나치지 않습니다.

# %%
arr = [1, '2', True, 'Hello', 3.1415926585]

for i in arr:
    print(i)

# %% [markdown]
# ### 함수 디버깅

# %%
def plus(x, y):
    val = x+y
    return val

print('더하기')
print(plus(10, 4))

# %%
def div(x, y):
    val = x/y
    return val

print('나누기')
print(div(10,1))

# %%



