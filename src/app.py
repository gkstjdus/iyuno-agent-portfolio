import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


st.set_page_config(
    page_title="AI 채용 데이터 분석",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI 기반 채용 데이터 분석 포트폴리오")
st.write(
    "채용 관련 데이터를 분석하고 AI/머신러닝을 활용하여 "
    "데이터 기반 인사이트를 제공하는 포트폴리오 프로젝트입니다."
)

st.sidebar.header("프로젝트 메뉴")

menu = st.sidebar.selectbox(
    "메뉴 선택",
    ["데이터 분석", "머신러닝 예측", "프로젝트 설명"]
)


# -------------------------
# 샘플 데이터 생성
# -------------------------

np.random.seed(42)

n = 100

experience = np.random.randint(0, 11, n)
projects = np.random.randint(0, 8, n)
certificates = np.random.randint(0, 4, n)

score = (
    experience * 5
    + projects * 7
    + certificates * 3
    + np.random.normal(0, 5, n)
)

df = pd.DataFrame({
    "experience": experience,
    "projects": projects,
    "certificates": certificates,
    "score": score.round(2)
})


# -------------------------
# 데이터 분석
# -------------------------

if menu == "데이터 분석":

    st.header("1. 채용 데이터 분석")

    st.dataframe(df.head(20))

    st.subheader("경력과 평가점수의 관계")

    fig, ax = plt.subplots()

    ax.scatter(
        df["experience"],
        df["score"]
    )

    ax.set_xlabel("경력 연차")
    ax.set_ylabel("평가 점수")
    ax.set_title("경력과 평가점수")

    st.pyplot(fig)

    st.subheader("주요 통계")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "평균 경력",
        f"{df['experience'].mean():.1f}년"
    )

    col2.metric(
        "평균 프로젝트 수",
        f"{df['projects'].mean():.1f}개"
    )

    col3.metric(
        "평균 평가점수",
        f"{df['score'].mean():.1f}"
    )


# -------------------------
# 머신러닝
# -------------------------

elif menu == "머신러닝 예측":

    st.header("2. 머신러닝 기반 평가점수 예측")

    X = df[
        ["experience", "projects", "certificates"]
    ]

    y = df["score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model.fit(
        X_train,
        y_train
    )

    prediction = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        prediction
    )

    r2 = r2_score(
        y_test,
        prediction
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "MAE",
        f"{mae:.2f}"
    )

    col2.metric(
        "R²",
        f"{r2:.2f}"
    )

    st.subheader("예측 결과")

    result = pd.DataFrame({
        "실제 점수": y_test.values,
        "예측 점수": prediction.round(2)
    })

    st.dataframe(result)


# -------------------------
# 프로젝트 설명
# -------------------------

else:

    st.header("3. 프로젝트 설명")

    st.markdown("""
    ### 프로젝트 목적

    채용공고에서 요구하는 데이터 분석 및 AI 활용 역량을
    실제 프로젝트 형태로 증명하기 위해 제작했습니다.

    ### 사용 기술

    - Python
    - Pandas
    - NumPy
    - Matplotlib
    - Scikit-learn
    - Streamlit

    ### AI 활용

    AI를 활용하여 프로젝트 구조를 설계하고,
    Python 코드 작성 및 오류 해결 과정에 활용했습니다.

    최종 코드는 직접 검토하고 실행 결과를 확인하여 수정했습니다.

    ### 기대 효과

    단순히 기술 목록을 나열하는 것이 아니라
    실제 데이터 분석과 머신러닝 모델 구현을 통해
    문제 해결 역량을 보여주는 것을 목표로 합니다.
    """)