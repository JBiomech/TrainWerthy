import json
from datetime import date
from io import BytesIO

import streamlit as st

st.set_page_config(page_title="James' Workout Diary", page_icon="🏋️", layout="wide")

PROGRAM = [
    {
        "week": 1,
        "focus": "Build rhythm and consistency",
        "sessions": [
            {
                "id": "w1a",
                "name": "Session A",
                "goal": "Lower body control + upper body pulling/pushing",
                "warmup": [
                    "Row 5–8 minutes at an easy/moderate pace",
                    "World's Greatest Stretch x 4–5 reps per side",
                ],
                "exercises": [
                    {"name": "Sit to Stand from Bench", "sets": 3, "reps": "10–12", "target": "20–25 kg", "notes": "Smooth control; stand tall each rep."},
                    {"name": "Assisted Pull-ups (standing on Superbad)", "sets": 3, "reps": "8–12", "target": "Band/height that allows 1–2 reps in reserve", "notes": "Choose assistance that keeps reps tidy."},
                    {"name": "Push-ups", "sets": 3, "reps": "8–12", "target": "Bodyweight", "notes": "Elevate hands if needed to keep form solid."},
                    {"name": "Leg Extension", "sets": 3, "reps": "12–15", "target": "25–30 kg", "notes": "Pause briefly at the top."},
                    {"name": "Plank", "sets": 3, "reps": "30–40 sec", "target": "Bodyweight", "notes": "Brace through ribs and glutes."},
                    {"name": "Side Plank", "sets": 2, "reps": "20–30 sec/side", "target": "Bodyweight", "notes": "Keep hips stacked."},
                ],
            },
            {
                "id": "w1b",
                "name": "Session B",
                "goal": "Squat pattern + horizontal press + single-leg strength",
                "warmup": [
                    "Row 5–8 minutes at an easy/moderate pace",
                    "World's Greatest Stretch x 4–5 reps per side",
                ],
                "exercises": [
                    {"name": "Hex Bar Squat", "sets": 4, "reps": "8", "target": "50–55 kg", "notes": "Controlled down, strong drive up."},
                    {"name": "DB Floor Press", "sets": 4, "reps": "8–10", "target": "15–17.5 kg each", "notes": "Leave 1–2 reps in reserve."},
                    {"name": "Bulgarian Split Squat", "sets": 3, "reps": "10/side", "target": "10–12.5 kg", "notes": "Keep torso tall; move steadily."},
                    {"name": "Crunches", "sets": 3, "reps": "15–20", "target": "Bodyweight", "notes": "Slow squeeze, do not rush."},
                    {"name": "Plank", "sets": 2, "reps": "30–40 sec", "target": "Bodyweight", "notes": "Optional extra if feeling good."},
                ],
            },
            {
                "id": "w1c",
                "name": "Session C",
                "goal": "Hip hinge + sit-to-stand + trunk work",
                "warmup": [
                    "Row 5–8 minutes at an easy/moderate pace",
                    "World's Greatest Stretch x 4–5 reps per side",
                ],
                "exercises": [
                    {"name": "Deadlift", "sets": 4, "reps": "6–8", "target": "45–50 kg", "notes": "Reset each rep; keep bar close."},
                    {"name": "Sit to Stand from Bench", "sets": 3, "reps": "12", "target": "20–25 kg", "notes": "Use the same or slightly lighter than Session A."},
                    {"name": "Assisted Pull-ups (standing on Superbad)", "sets": 3, "reps": "8–10", "target": "Same assistance as Session A", "notes": "Stop before form breaks."},
                    {"name": "Sit-ups", "sets": 3, "reps": "12–15", "target": "6 kg ball", "notes": "Exhale on the way up."},
                    {"name": "Side Plank", "sets": 2, "reps": "20–30 sec/side", "target": "Bodyweight", "notes": "Optional top leg in front for stability."},
                ],
            },
        ],
    },
    {
        "week": 2,
        "focus": "Slight progression if Week 1 feels comfortable",
        "sessions": [
            {
                "id": "w2a",
                "name": "Session A",
                "goal": "Repeat and progress modestly",
                "warmup": [
                    "Row 5–8 minutes at an easy/moderate pace",
                    "World's Greatest Stretch x 4–5 reps per side",
                ],
                "exercises": [
                    {"name": "Sit to Stand from Bench", "sets": 3, "reps": "12", "target": "22.5–27.5 kg", "notes": "Only add load if Week 1 moved well."},
                    {"name": "Assisted Pull-ups (standing on Superbad)", "sets": 3, "reps": "10–12", "target": "Slightly less assistance if able", "notes": "Keep range consistent."},
                    {"name": "Push-ups", "sets": 3, "reps": "10–12", "target": "Bodyweight", "notes": "Elevate less if Week 1 was strong."},
                    {"name": "Leg Extension", "sets": 3, "reps": "12–15", "target": "30 kg", "notes": "Controlled squeeze at the top."},
                    {"name": "Plank", "sets": 3, "reps": "35–45 sec", "target": "Bodyweight", "notes": "Maintain steady breathing."},
                    {"name": "Side Plank", "sets": 2, "reps": "25–30 sec/side", "target": "Bodyweight", "notes": "Quality over duration."},
                ],
            },
            {
                "id": "w2b",
                "name": "Session B",
                "goal": "Build on squat/press confidence",
                "warmup": [
                    "Row 5–8 minutes at an easy/moderate pace",
                    "World's Greatest Stretch x 4–5 reps per side",
                ],
                "exercises": [
                    {"name": "Hex Bar Squat", "sets": 4, "reps": "8", "target": "55–60 kg", "notes": "Only progress if all Week 1 sets felt controlled."},
                    {"name": "DB Floor Press", "sets": 4, "reps": "8–10", "target": "17.5–20 kg each", "notes": "Pause lightly on the floor."},
                    {"name": "Bulgarian Split Squat", "sets": 3, "reps": "10–12/side", "target": "12.5 kg", "notes": "Keep front foot rooted."},
                    {"name": "Crunches", "sets": 3, "reps": "18–20", "target": "Bodyweight", "notes": "Do not pull the neck."},
                    {"name": "Plank", "sets": 2, "reps": "35–45 sec", "target": "Bodyweight", "notes": "Optional finisher."},
                ],
            },
            {
                "id": "w2c",
                "name": "Session C",
                "goal": "Hinge progression with stable technique",
                "warmup": [
                    "Row 5–8 minutes at an easy/moderate pace",
                    "World's Greatest Stretch x 4–5 reps per side",
                ],
                "exercises": [
                    {"name": "Deadlift", "sets": 4, "reps": "6–8", "target": "50–55 kg", "notes": "No grinding reps."},
                    {"name": "Sit to Stand from Bench", "sets": 3, "reps": "12", "target": "22.5–27.5 kg", "notes": "Same guidance as Session A."},
                    {"name": "Assisted Pull-ups (standing on Superbad)", "sets": 3, "reps": "8–10", "target": "Same or slightly less assistance than Week 1", "notes": "Stay smooth."},
                    {"name": "Sit-ups", "sets": 3, "reps": "12–15", "target": "6–9 kg ball", "notes": "Use 9 kg only if 6 kg felt solid."},
                    {"name": "Side Plank", "sets": 2, "reps": "25–30 sec/side", "target": "Bodyweight", "notes": "Keep shoulders stacked."},
                ],
            },
        ],
    },
    {
        "week": 3,
        "focus": "Keep progress gentle and repeatable",
        "sessions": [
            {
                "id": "w3a",
                "name": "Session A",
                "goal": "More confidence with repeated patterns",
                "warmup": [
                    "Row 5–8 minutes at an easy/moderate pace",
                    "World's Greatest Stretch x 4–5 reps per side",
                ],
                "exercises": [
                    {"name": "Sit to Stand from Bench", "sets": 3, "reps": "12–15", "target": "25–30 kg", "notes": "Stay below max effort."},
                    {"name": "Assisted Pull-ups (standing on Superbad)", "sets": 3, "reps": "10–12", "target": "Band/height that makes last 2 reps challenging but clean", "notes": "Good posture at top and bottom."},
                    {"name": "Push-ups", "sets": 3, "reps": "10–15", "target": "Bodyweight", "notes": "Stop 1 rep before form changes."},
                    {"name": "Leg Extension", "sets": 3, "reps": "12–15", "target": "30–35 kg", "notes": "Choose the lower end if knee comfort is better there."},
                    {"name": "Plank", "sets": 3, "reps": "40–50 sec", "target": "Bodyweight", "notes": "Maintain a straight line."},
                    {"name": "Side Plank", "sets": 2, "reps": "25–35 sec/side", "target": "Bodyweight", "notes": "Shorter holds are fine if cleaner."},
                ],
            },
            {
                "id": "w3b",
                "name": "Session B",
                "goal": "Solidify squat and press workload",
                "warmup": [
                    "Row 5–8 minutes at an easy/moderate pace",
                    "World's Greatest Stretch x 4–5 reps per side",
                ],
                "exercises": [
                    {"name": "Hex Bar Squat", "sets": 4, "reps": "8", "target": "60–65 kg", "notes": "Only progress if previous week stayed crisp."},
                    {"name": "DB Floor Press", "sets": 4, "reps": "8–10", "target": "17.5–20 kg each", "notes": "Use 20 kg only if the full set is controlled."},
                    {"name": "Bulgarian Split Squat", "sets": 3, "reps": "12/side", "target": "12.5–15 kg", "notes": "Choose the load that lets both sides match."},
                    {"name": "Crunches", "sets": 3, "reps": "20", "target": "Bodyweight", "notes": "Slow down each rep."},
                    {"name": "Plank", "sets": 2, "reps": "40 sec", "target": "Bodyweight", "notes": "Optional finisher."},
                ],
            },
            {
                "id": "w3c",
                "name": "Session C",
                "goal": "Repeat hinge day with slight lift",
                "warmup": [
                    "Row 5–8 minutes at an easy/moderate pace",
                    "World's Greatest Stretch x 4–5 reps per side",
                ],
                "exercises": [
                    {"name": "Deadlift", "sets": 4, "reps": "6", "target": "55–60 kg", "notes": "Do not chase the top number if speed slows a lot."},
                    {"name": "Sit to Stand from Bench", "sets": 3, "reps": "12", "target": "25–30 kg", "notes": "Steady tempo."},
                    {"name": "Assisted Pull-ups (standing on Superbad)", "sets": 3, "reps": "8–10", "target": "Same as Week 3 Session A", "notes": "Clean reps beat extra reps."},
                    {"name": "Sit-ups", "sets": 3, "reps": "15", "target": "6–9 kg ball", "notes": "Use the lower load if it keeps the movement better."},
                    {"name": "Side Plank", "sets": 2, "reps": "25–35 sec/side", "target": "Bodyweight", "notes": "Keep neck relaxed."},
                ],
            },
        ],
    },
    {
        "week": 4,
        "focus": "Consolidate, not test",
        "sessions": [
            {
                "id": "w4a",
                "name": "Session A",
                "goal": "Repeat best sustainable version of the month",
                "warmup": [
                    "Row 5–8 minutes at an easy/moderate pace",
                    "World's Greatest Stretch x 4–5 reps per side",
                ],
                "exercises": [
                    {"name": "Sit to Stand from Bench", "sets": 3, "reps": "10–12", "target": "25–30 kg", "notes": "Repeat the best Week 3 load, no need to push past it."},
                    {"name": "Assisted Pull-ups (standing on Superbad)", "sets": 3, "reps": "8–12", "target": "Best clean assistance level from the month", "notes": "Keep all reps tidy."},
                    {"name": "Push-ups", "sets": 3, "reps": "10–15", "target": "Bodyweight", "notes": "Match or slightly beat best clean set."},
                    {"name": "Leg Extension", "sets": 3, "reps": "12–15", "target": "30–35 kg", "notes": "Comfortable range only."},
                    {"name": "Plank", "sets": 3, "reps": "40–50 sec", "target": "Bodyweight", "notes": "Strong brace throughout."},
                    {"name": "Side Plank", "sets": 2, "reps": "25–35 sec/side", "target": "Bodyweight", "notes": "Stop before hips drop."},
                ],
            },
            {
                "id": "w4b",
                "name": "Session B",
                "goal": "Repeat strong, comfortable squat and press",
                "warmup": [
                    "Row 5–8 minutes at an easy/moderate pace",
                    "World's Greatest Stretch x 4–5 reps per side",
                ],
                "exercises": [
                    {"name": "Hex Bar Squat", "sets": 4, "reps": "6–8", "target": "60–65 kg", "notes": "Use a load that stays powerful, not maximal."},
                    {"name": "DB Floor Press", "sets": 4, "reps": "8", "target": "17.5–20 kg each", "notes": "Stay 1–2 reps away from failure."},
                    {"name": "Bulgarian Split Squat", "sets": 3, "reps": "10–12/side", "target": "12.5–15 kg", "notes": "Controlled tempo."},
                    {"name": "Crunches", "sets": 3, "reps": "18–20", "target": "Bodyweight", "notes": "Smooth, consistent reps."},
                    {"name": "Plank", "sets": 2, "reps": "40 sec", "target": "Bodyweight", "notes": "Optional finisher."},
                ],
            },
            {
                "id": "w4c",
                "name": "Session C",
                "goal": "Finish with a clean hinge session",
                "warmup": [
                    "Row 5–8 minutes at an easy/moderate pace",
                    "World's Greatest Stretch x 4–5 reps per side",
                ],
                "exercises": [
                    {"name": "Deadlift", "sets": 4, "reps": "5–6", "target": "55–60 kg", "notes": "Stay with the cleanest strong load from the month."},
                    {"name": "Sit to Stand from Bench", "sets": 3, "reps": "12", "target": "25–30 kg", "notes": "Repeat best quality load."},
                    {"name": "Assisted Pull-ups (standing on Superbad)", "sets": 3, "reps": "8–10", "target": "Best clean assistance level from the month", "notes": "Keep the final reps smooth."},
                    {"name": "Sit-ups", "sets": 3, "reps": "12–15", "target": "6–9 kg ball", "notes": "Only go heavier if movement stays controlled."},
                    {"name": "Side Plank", "sets": 2, "reps": "25–35 sec/side", "target": "Bodyweight", "notes": "Finish on good quality."},
                ],
            },
        ],
    },
]


def build_initial_log():
    data = {}
    for week in PROGRAM:
        for session in week["sessions"]:
            data[session["id"]] = {
                "completed": False,
                "date": "",
                "session_comment": "",
                "coach_comment": "",
                "exercises": [
                    {"achieved": "", "comments": ""} for _ in session["exercises"]
                ],
            }
    return data


def export_json_bytes(payload: dict) -> bytes:
    return json.dumps(payload, indent=2).encode("utf-8")


def merge_imported_data(imported: dict) -> dict:
    base = build_initial_log()
    for session_id, session_data in imported.items():
        if session_id in base and isinstance(session_data, dict):
            merged_session = base[session_id]
            merged_session.update({
                "completed": session_data.get("completed", merged_session["completed"]),
                "date": session_data.get("date", merged_session["date"]),
                "session_comment": session_data.get("session_comment", merged_session["session_comment"]),
                "coach_comment": session_data.get("coach_comment", merged_session["coach_comment"]),
            })
            imported_exercises = session_data.get("exercises", [])
            for idx, exercise_entry in enumerate(imported_exercises):
                if idx < len(merged_session["exercises"]) and isinstance(exercise_entry, dict):
                    merged_session["exercises"][idx]["achieved"] = exercise_entry.get("achieved", "")
                    merged_session["exercises"][idx]["comments"] = exercise_entry.get("comments", "")
    return base


if "log" not in st.session_state:
    st.session_state.log = build_initial_log()

st.title("🏋️ Client Workout Diary")
st.caption("4-week programme · 3 sessions per week · Python/Streamlit version")

with st.sidebar:
    st.header("Diary controls")

    uploaded = st.file_uploader("Import diary JSON", type=["json"])
    if uploaded is not None:
        try:
            imported_payload = json.load(uploaded)
            st.session_state.log = merge_imported_data(imported_payload)
            st.success("Diary imported.")
        except Exception:
            st.error("That file could not be read as a valid diary JSON.")

    completed_count = sum(1 for x in st.session_state.log.values() if x["completed"])
    st.metric("Sessions completed", f"{completed_count}/12")
    st.progress(completed_count / 12)

    exported = export_json_bytes(st.session_state.log)
    st.download_button(
        "Export diary JSON",
        data=exported,
        file_name=f"workout-diary-{date.today().isoformat()}.json",
        mime="application/json",
        use_container_width=True,
    )

    st.info(
        "Client can fill this in, export the JSON file, and send it to you. "
        "You can re-import it, add coach comments, and export it back."
    )

weeks = [f"Week {week['week']}" for week in PROGRAM]
selected_week_label = st.selectbox("Select week", weeks)
selected_week = next(week for week in PROGRAM if f"Week {week['week']}" == selected_week_label)

session_names = [session["name"] for session in selected_week["sessions"]]
selected_session_name = st.radio("Select session", session_names, horizontal=True)
selected_session = next(session for session in selected_week["sessions"] if session["name"] == selected_session_name)
diary = st.session_state.log[selected_session["id"]]

col1, col2 = st.columns([1.4, 1])

with col1:
    st.subheader(f"{selected_session['name']} — {selected_session['goal']}")

    with st.container(border=True):
        st.markdown("**Always before the workout**")
        for item in selected_session["warmup"]:
            st.write(f"- {item}")

    for idx, exercise in enumerate(selected_session["exercises"]):
        with st.expander(f"{exercise['name']} · {exercise['sets']} sets · {exercise['reps']} · target: {exercise['target']}", expanded=(idx == 0)):
            info_col, entry_col = st.columns(2)
            with info_col:
                st.markdown("**Planned**")
                st.write(f"Sets: {exercise['sets']}")
                st.write(f"Reps: {exercise['reps']}")
                st.write(f"Target load/level: {exercise['target']}")
                st.write(f"Coach note: {exercise['notes']}")
            with entry_col:
                achieved = st.text_input(
                    f"Achievement for {exercise['name']}",
                    value=diary["exercises"][idx]["achieved"],
                    key=f"achieved_{selected_session['id']}_{idx}",
                    placeholder="Example: 3 x 12 @ 25 kg",
                )
                comments = st.text_area(
                    f"Comments for {exercise['name']}",
                    value=diary["exercises"][idx]["comments"],
                    key=f"comments_{selected_session['id']}_{idx}",
                    placeholder="How did it feel? Any pain, confidence issue, or win?",
                    height=120,
                )
                st.session_state.log[selected_session["id"]]["exercises"][idx]["achieved"] = achieved
                st.session_state.log[selected_session["id"]]["exercises"][idx]["comments"] = comments

with col2:
    st.subheader("Session diary")
    diary_date = st.date_input(
        "Workout date",
        value=date.fromisoformat(diary["date"]) if diary["date"] else date.today(),
        key=f"date_{selected_session['id']}",
    )
    st.session_state.log[selected_session["id"]]["date"] = diary_date.isoformat()

    completed = st.checkbox(
        "Mark session as completed",
        value=diary["completed"],
        key=f"completed_{selected_session['id']}",
    )
    st.session_state.log[selected_session["id"]]["completed"] = completed

    session_comment = st.text_area(
        "Client session comments",
        value=diary["session_comment"],
        key=f"session_comment_{selected_session['id']}",
        placeholder="Example: felt strong on squats, left knee a little stiff, rowing felt easier today.",
        height=160,
    )
    st.session_state.log[selected_session["id"]]["session_comment"] = session_comment

    coach_comment = st.text_area(
        "Coach review comments",
        value=diary["coach_comment"],
        key=f"coach_comment_{selected_session['id']}",
        placeholder="Coach can add review comments after importing the diary file.",
        height=160,
    )
    st.session_state.log[selected_session["id"]]["coach_comment"] = coach_comment

    st.warning(
        "Suggested effort: finish most working sets with around 1–2 reps left in reserve. "
        "If anything feels painful or unusually unstable, reduce the load, shorten the range, or stop and note it."
    )

st.divider()
