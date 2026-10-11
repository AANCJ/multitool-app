import streamlit as st

st.title("🌟 Ayaansh's Multi-Tool App")
st.write(
    "Welcome! Choose one of your custom tools from the dropdown menu below."
)

# Main menu selection using a dropdown box
option = st.selectbox(
    "Press / Choose a tool:",
    [
        "Select a tool...",
        "1. Factorial Finder",
        "2. Prime Number Finder",
        "3. Average Number-er",
        "4. Ice Cream Bot (Ayaansh)",
        "5. Calculator",
        "6. Leap Year Checker",
        "7. Number of Input Checker",
        "8. Year to Days and Hours Converter",
        "9. Odd or Even Checker",
    ],
)

# --- TOOL 1: Factorial Finder ---
if option == "1. Factorial Finder":
  st.subheader("Factorial Finder")
  x = st.number_input("Enter number to find factorials", min_value=0, step=1)
  if st.button("Calculate Factorial"):
    f = 1
    for i in range(1, int(x) + 1):
      f = f * i
    st.success(f"The factorial total is {f}")

# --- TOOL 2: Prime Number Finder ---
elif option == "2. Prime Number Finder":
  st.subheader("Prime Number Finder")
  x = st.number_input("Enter your number", min_value=1, step=1)
  if st.button("Check Prime"):
    f = 0
    for i in range(1, int(x) + 1):
      if x % i == 0:
        f = f + 1
    if f == 1:
      st.info("Not prime or composite")
    elif f == 2:
      st.success("It is prime")
    else:
      st.warning("It is composite")

# --- TOOL 3: Average Number-er ---
elif option == "3. Average Number-er":
  st.subheader("Average Number-er")
  q = st.number_input(
      "Number of integers you want to average", min_value=1, step=1
  )
  # Using text input or fields for list logic in web apps
  numbers_input = st.text_input(
      "Enter integers separated by spaces (e.g., 10 20 30):"
  )
  if st.button("Calculate Average"):
    try:
      nums = [int(n) for n in numbers_input.split()]
      if len(nums) > 0:
        t = sum(nums)
        st.success(f"Total sum or average is ::: {t / 10}")
      else:
        st.error("Please enter valid integers.")
    except ValueError:
      st.error("Please enter numbers separated by spaces.")

# --- TOOL 4: Ice Cream Bot ---
elif option == "4. Ice Cream Bot (Ayaansh)":
  st.subheader("Chat with Ayaansh's Bot")
  name = st.text_input("What is your name:")
  if name:
    st.write(f"Hi {name}, Nic to meet you. I am Ayaansh")
    fav_ice = st.text_input("What is your favorite ice cream flavor:")
    if fav_ice:
      st.success(f"{fav_ice}! I like oreo 🍪")

# --- TOOL 5: Calculator ---
elif option == "5. Calculator":
  st.subheader("Simple Calculator")
  x = st.number_input("Enter a number:", value=0.0)
  y = st.number_input("Enter another number:", value=0.0)
  z = st.selectbox("What would you like to do?", ["+", "-", "*", "/"])

  if st.button("Calculate Result"):
    if z == "+":
      st.success(f"Your answer is {x + y}")
    elif z == "-":
      st.success(f"Your answer is {x - y}")
    elif z == "*":
      st.success(f"Your answer is {x * y}")
    elif z == "/":
      if y != 0:
        st.success(f"Your answer is {x / y}")
      else:
        st.error("Error: Division by zero!")

# --- TOOL 6: Leap Year Checker ---
elif option == "6. Leap Year Checker":
  st.subheader("Leap Year Checker")
  x = st.number_input("Enter the year", min_value=0, step=1)
  if st.button("Check Year"):
    is_leap = False
    if x % 4 == 0:
      is_leap = True
    if x % 100 == 0:
      is_leap = False
    if x % 400 == 0:
      is_leap = True

    if is_leap:
      st.success(f"{int(x)} is a leap year")
    else:
      st.info(f"{int(x)} is not a leap year")

# --- TOOL 7: Number of Input Checker ---
elif option == "7. Number of Input Checker":
  st.subheader("Number of Input Checker")
  st.write(
      "Enter numbers one by one. Enter a negative number to stop and see totals."
  )

  # Using session state to track inputs in Streamlit web interface
  if "inputs_list" not in st.session_state:
    st.session_state.inputs_list = []

  val = st.number_input("Enter a number (negative to stop):", step=1, key="num_in")
  col1, col2 = st.columns(2)

  with col1:
    if st.button("Add Number"):
      if val < 0:
        st.warning("Program Stopped (Negative number entered)")
      else:
        st.session_state.inputs_list.append(val)
        st.success(f"Added {val}!")

  with col2:
    if st.button("Reset Inputs"):
      st.session_state.inputs_list = []
      st.rerun()

  if st.session_state.inputs_list:
    st.write("Current inputs:", st.session_state.inputs_list)
    st.write("Total of all inputs are:", sum(st.session_state.inputs_list))
    st.write("Number of inputs are:", len(st.session_state.inputs_list))

# --- TOOL 8: Year to Days and Hours Converter ---
elif option == "8. Year to Days and Hours Converter":
  st.subheader("Time Converter")
  x = st.number_input("Enter number of years", min_value=0, step=1)
  if st.button("Convert"):
    d = x * 365
    h = d * 24
    st.success(f"Number of days are {int(d)} and number of hours are {int(h)}")

# --- TOOL 9: Odd or Even Checker ---
elif option == "9. Odd or Even Checker":
  st.subheader("Odd or Even Checker")
  x = st.number_input("Enter your odd or even number:", step=1)
  if st.button("Check Odd/Even"):
    if x % 2 == 0:
      st.success(f"The number entered ({int(x)}) is even")
    else:
      st.success(f"Your number ({int(x)}) is odd")