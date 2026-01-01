import streamlit as st

# ================= INITIAL DATA =================
if 'bank_data' not in st.session_state:
    st.session_state.bank_data = {}

bank_data = st.session_state.bank_data

st.title("🏦 POCKIE BANK – STREAMLIT APP")
st.write("Simple Bank Management System using Streamlit")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Check Balance",
        "Update Account",
        "Delete Account"
    ]
)

# ================= CREATE ACCOUNT =================
if menu == "Create Account":
    st.subheader("Create New Account")

    acc_no = st.text_input("Account Number")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    aadhar = st.text_input("Aadhar Number")
    balance = st.number_input("Opening Balance", min_value=0, step=100)

    if st.button("Create Account"):
        if acc_no in bank_data:
            st.error("Account already exists")
        elif acc_no == "":
            st.warning("Account number is required")
        else:
            bank_data[acc_no] = {
                'name': name,
                'age': age,
                'aadhar_no': aadhar,
                'balance': balance
            }
            st.success("Account created successfully")

# ================= DEPOSIT MONEY =================
elif menu == "Deposit Money":
    st.subheader("Deposit Money")

    acc_no = st.text_input("Account Number")
    amount = st.number_input("Deposit Amount", min_value=1, step=100)

    if st.button("Deposit"):
        if acc_no not in bank_data:
            st.error("Account not found")
        else:
            bank_data[acc_no]['balance'] += amount
            st.success(f"Updated Balance: ₹{bank_data[acc_no]['balance']}")

# ================= WITHDRAW MONEY =================
elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")

    acc_no = st.text_input("Account Number")
    amount = st.number_input("Withdraw Amount", min_value=1, step=100)

    if st.button("Withdraw"):
        if acc_no not in bank_data:
            st.error("Account not found")
        elif amount > bank_data[acc_no]['balance']:
            st.error("Insufficient balance")
        else:
            bank_data[acc_no]['balance'] -= amount
            st.success(f"Remaining Balance: ₹{bank_data[acc_no]['balance']}")

# ================= CHECK BALANCE =================
elif menu == "Check Balance":
    st.subheader("Check Balance")

    acc_no = st.text_input("Account Number")

    if st.button("Check"):
        if acc_no not in bank_data:
            st.error("Account not found")
        else:
            st.info(f"Total Balance: ₹{bank_data[acc_no]['balance']}")

# ================= UPDATE ACCOUNT =================
elif menu == "Update Account":
    st.subheader("Update Account")

    acc_no = st.text_input("Account Number")

    if acc_no in bank_data:
        update_choice = st.selectbox("Update Field", ["Name", "Age"])

        if update_choice == "Name":
            new_name = st.text_input("New Name")
            if st.button("Update Name"):
                bank_data[acc_no]['name'] = new_name
                st.success("Name updated successfully")

        elif update_choice == "Age":
            new_age = st.number_input("New Age", min_value=1, step=1)
            if st.button("Update Age"):
                bank_data[acc_no]['age'] = new_age
                st.success("Age updated successfully")
    else:
        if acc_no:
            st.error("Account not found")

# ================= DELETE ACCOUNT =================
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc_no = st.text_input("Account Number")

    if st.button("Delete"):
        if acc_no not in bank_data:
            st.error("Account not found")
        else:
            del bank_data[acc_no]
            st.success("Account deleted successfully")

st.sidebar.markdown("---")
st.sidebar.write("© Pockie Bank Streamlit App")