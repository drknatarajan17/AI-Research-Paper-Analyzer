import streamlit as st
import fitz

st.set_page_config(
    page_title="AI Research Paper Analyzer",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Research Paper Analyzer")

st.sidebar.title("📚 Research Analyzer")
st.sidebar.success("Phase 2 Active")
st.sidebar.markdown("---")
st.sidebar.write("Features")

st.markdown(
    "Upload a research paper PDF and extract basic information."
)

uploaded_file = st.file_uploader(
    "Upload Research Paper",
    type=["pdf"]
)

if uploaded_file is not None:

    pdf = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in pdf:
        text += page.get_text()

    st.success("PDF Loaded Successfully")

    # Title Detection
    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    st.subheader("📌 Detected Title")

    if len(lines) > 0:
        st.success(lines[0])

    # Authors
    st.subheader("👨‍🔬 Possible Authors")

    if len(lines) > 1:
        st.info(lines[1])

    # Text Preview
    st.subheader("📄 Extracted Text Preview")

    st.text_area(
        "Paper Content",
        text[:5000],
        height=350
    )

    # Abstract Detection
    st.subheader("📄 Abstract")

    text_lower = text.lower()

    if "abstract" in text_lower:

        start = text_lower.find("abstract")

        abstract = text[start:start+2000]

        st.text_area(
            "Abstract Content",
            abstract,
            height=200
        )

    else:

        st.warning(
            "Abstract section not detected."
        )

    # Keywords
    st.subheader("🔑 Keywords")

    words = text.split()

    keywords = []

    for word in words:

        word = word.strip()

        if len(word) > 8:
            keywords.append(word)

    unique_keywords = list(
        dict.fromkeys(keywords)
    )

    st.write(unique_keywords[:20])

    # Statistics
    st.subheader("📊 Research Paper Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Characters",
            len(text)
        )

    with col2:
        st.metric(
            "Words",
            len(text.split())
        )

    with col3:
        st.metric(
            "Pages",
            len(pdf)
        )


st.subheader("📝 AI Research Summary")

sentences = text.split(".")

summary = ""

for sentence in sentences[:10]:

    summary += sentence + ". "

st.text_area(
    "Generated Summary",
    summary,
    height=250
)
st.subheader("🎯 Research Objectives")

objective_keywords = [
    "objective",
    "aim",
    "purpose",
    "goal",
    "proposed"
]

found = False

for sentence in text.split("."):

    for keyword in objective_keywords:

        if keyword.lower() in sentence.lower():

            st.success(sentence.strip())

            found = True

            break

if not found:

    st.warning(
        "Objectives not automatically detected."
    )
st.subheader("⚙ Methodology")

method_keywords = [
    "method",
    "methodology",
    "algorithm",
    "framework",
    "approach",
    "model"
]

found = False

for sentence in text.split("."):

    for keyword in method_keywords:

        if keyword.lower() in sentence.lower():

            st.info(sentence.strip())

            found = True

            break

if not found:

    st.warning(
        "Methodology not detected."
    )
st.subheader("🔍 Research Gap Analysis")

gap_keywords = [
    "future work",
    "future scope",
    "limitation",
    "limitations",
    "challenge",
    "challenges"
]

found = False

for sentence in text.split("."):

    for keyword in gap_keywords:

        if keyword.lower() in sentence.lower():

            st.warning(sentence.strip())

            found = True

            break

if not found:

    st.info(
        "No explicit research gaps detected."
    )
st.subheader("⭐ Reviewer Dashboard")

word_count = len(text.split())

novelty = min(
    10,
    round(word_count / 1000 + 5, 1)
)

technical = min(
    10,
    round(word_count / 1200 + 5, 1)
)

c1, c2 = st.columns(2)

with c1:
    st.metric(
        "Novelty Score",
        novelty
    )

with c2:
    st.metric(
        "Technical Score",
        technical
    )

if novelty >= 8:

    st.success(
        "Recommendation: Accept with Minor Revision"
    )

elif novelty >= 6:

    st.warning(
        "Recommendation: Major Revision"
    )

else:

    st.error(
        "Recommendation: Reject"
    )

