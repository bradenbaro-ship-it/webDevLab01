import streamlit as st
import info
import pandas as pd

st.set_page_config(page_title="Portfolio")

st.title("Portfolio")
st.image(info.profile_picture, width=160, caption="Profile")

st.write(info.about_me)

st.subheader("Links")
link_cols = st.columns(3)
with link_cols[0]:
    st.image(info.linkedin_image_url, width=28)
    st.markdown(f"[LinkedIn]({info.my_linkedin_url})")
with link_cols[1]:
    st.image(info.github_image_url, width=28)
    st.markdown(f"[GitHub]({info.my_github_url})")
with link_cols[2]:
    st.image(info.email_image_url, width=28)
    st.markdown(f"[Email](mailto:{info.my_email_address})")

st.divider()

st.header("Education")
edu_cols = st.columns(2)
with edu_cols[0]:
    st.write(f"**{info.education_data['Degree']}**")
    st.write(info.education_data['Institution'])
    st.write(info.education_data['Location'])
with edu_cols[1]:
    st.metric("GPA", info.education_data['GPA'])
    st.write(f"Expected Graduation: {info.education_data['Graduation Date']}")

st.divider()

st.header("Experience")
for job, (details, image) in info.experience_data.items():
    exp_cols = st.columns([2, 1])
    with exp_cols[0]:
        st.subheader(job)
        for bullet in details:
            st.write(bullet)
    with exp_cols[1]:
        st.image(image, width=160)

st.divider()

st.header("Courses and Key Skills")
for code, name, sem, skill in zip(
    info.course_data["code"],
    info.course_data["names"],
    info.course_data["semester_taken"],
    info.course_data["skills"]
):
    st.write(f"**{code} - {name}** ({sem} semester)")
    st.caption(skill)

st.divider()

st.header("Projects")
for proj, desc in info.projects_data.items():
    st.markdown(f"**{proj}** — {desc}")

st.divider()

st.header("Programming Skills")
prog_cols = st.columns(len(info.programming_data))
for i, (lang, level) in enumerate(info.programming_data.items()):
    with prog_cols[i]:
        icon = info.programming_icons.get(lang, "")
        st.metric(f"{lang}", f"{level}%")
        st.progress(level)

st.divider()

st.header("Languages")
for lang, fluency in info.spoken_data.items():
    flag = info.spoken_icons.get(lang, "")
    st.write(f"{lang}: {fluency}")

st.divider()

st.header("Leadership and Activities")
for role, (details, image) in info.leadership_data.items():
    st.subheader(role)
    st.image(image, width=160)
    for bullet in details:
        st.write(bullet)

for act, bullets in info.activity_data.items():
    st.subheader(act)
    for bullet in bullets:
        st.write(bullet)

st.divider()
st.caption("Portfolio generated using Streamlit and info.py")
