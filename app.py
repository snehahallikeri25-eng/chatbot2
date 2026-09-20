import streamlit as st
from datetime import datetime

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Banking Assistant",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# DEMO ACCOUNT DATA
# ============================================================

ACCOUNT = {
    "name": "Chiya",
    "account_number": "1234567890",
    "account_type": "Savings Account",
    "balance": 25000.00,
    "ifsc": "DEMO0001234",
    "branch": "Demo Main Branch",
    "phone": "+91 XXXXX XXXXX",
    "email": "chiya@example.com",
    "customer_id": "DEMO-CUST-001"
}

INITIAL_TRANSACTIONS = [
    {
        "date": "18 Sep 2026",
        "description": "Scholarship",
        "type": "Credit",
        "amount": 2000.00
    },
    {
        "date": "17 Sep 2026",
        "description": "UPI Payment",
        "type": "Debit",
        "amount": 500.00
    },
    {
        "date": "15 Sep 2026",
        "description": "Cash Deposit",
        "type": "Credit",
        "amount": 1500.00
    },
    {
        "date": "13 Sep 2026",
        "description": "Online Purchase",
        "type": "Debit",
        "amount": 750.00
    }
]

# ============================================================
# SESSION STATE
# ============================================================

if "balance" not in st.session_state:
    st.session_state.balance = ACCOUNT["balance"]

if "transactions" not in st.session_state:
    st.session_state.transactions = INITIAL_TRANSACTIONS.copy()

if "verified" not in st.session_state:
    st.session_state.verified = False

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {
            "role": "assistant",
            "content": (
                "👋 Welcome to the AI Banking Assistant!\n\n"
                "This is a demo banking application. "
                "You can explore the banking services using the menu."
            )
        }
    ]

if "transfer_message" not in st.session_state:
    st.session_state.transfer_message = ""

if "upi_message" not in st.session_state:
    st.session_state.upi_message = ""

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f4f7fb;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}

.header {
    background: linear-gradient(135deg, #0b1f3a, #1261a0);
    padding: 22px;
    border-radius: 15px;
    color: white;
    margin-bottom: 20px;
}

.header h1 {
    margin: 0;
    font-size: 30px;
}

.header p {
    margin: 5px 0 0 0;
    opacity: 0.9;
}

.online {
    color: #55efc4;
    font-weight: bold;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.balance-card {
    background: linear-gradient(135deg, #0b1f3a, #1261a0);
    color: white;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
}

.balance-amount {
    font-size: 36px;
    font-weight: bold;
}

.section-title {
    font-size: 25px;
    font-weight: bold;
    color: #0b1f3a;
    margin-bottom: 15px;
}

.demo-note {
    background: #fff3cd;
    padding: 12px;
    border-radius: 10px;
    border-left: 5px solid #ffc107;
    color: #664d03;
    margin-bottom: 15px;
}

.success-box {
    background: #d1e7dd;
    padding: 12px;
    border-radius: 10px;
    color: #0f5132;
}

.info-box {
    background: #cff4fc;
    padding: 12px;
    border-radius: 10px;
    color: #055160;
}

.danger-box {
    background: #f8d7da;
    padding: 12px;
    border-radius: 10px;
    color: #842029;
}

.chat-box {
    background: white;
    padding: 15px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="header">
    <h1>🏦 AI Banking Assistant</h1>
    <p>Smart • Secure • Interactive Banking</p>
    <p class="online">● Online — Demo Mode</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="demo-note">
<b>⚠️ DEMO APPLICATION</b><br>
This application uses fictional account information.
No real banking account, money transfer, UPI transaction,
or financial transaction is performed.
</div>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🏦 Banking Services")

menu = st.sidebar.radio(
    "Select Service",
    [
        "🏠 Dashboard",
        "👤 Account Details",
        "💰 Balance",
        "📊 Transactions",
        "📱 UPI Payments",
        "💸 Money Transfer",
        "💳 Cards",
        "🏧 ATM Services",
        "🏦 Loans",
        "💵 Deposits",
        "🔐 Security",
        "🏢 IFSC",
        "📞 Customer Support",
        "🤖 AI Chatbot"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Demo Login\n\n"
    "Name: Chiya\n"
    "Account: 1234567890"
)

if st.sidebar.button("🔄 Reset Demo"):
    st.session_state.balance = ACCOUNT["balance"]
    st.session_state.transactions = INITIAL_TRANSACTIONS.copy()
    st.session_state.verified = False
    st.session_state.chat_messages = [
        {
            "role": "assistant",
            "content": "👋 Demo has been reset successfully."
        }
    ]
    st.rerun()

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def add_transaction(description, transaction_type, amount):
    transaction = {
        "date": datetime.now().strftime("%d %b %Y"),
        "description": description,
        "type": transaction_type,
        "amount": float(amount)
    }

    st.session_state.transactions.insert(0, transaction)


def verify_user():
    st.markdown("### 🔐 Demo Account Verification")

    name = st.text_input(
        "Enter Account Holder Name",
        placeholder="Enter Chiya"
    )

    account_number = st.text_input(
        "Enter Demo Account Number",
        placeholder="10 digit demo account number",
        max_chars=10
    )

    if st.button("Verify Account", type="primary"):

        if name.strip().lower() != ACCOUNT["name"].lower():
            st.error("❌ Account holder name does not match.")

        elif account_number != ACCOUNT["account_number"]:
            st.error("❌ Account number does not match.")

        else:
            st.session_state.verified = True
            st.success("✅ Demo account verified successfully!")
            st.rerun()


def require_verification():
    if not st.session_state.verified:
        st.warning("🔐 Please verify the demo account to view protected details.")
        verify_user()
        return False

    return True


# ============================================================
# DASHBOARD
# ============================================================

if menu == "🏠 Dashboard":

    st.markdown(
        '<div class="section-title">🏠 Banking Dashboard</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Available Balance",
            f"₹{st.session_state.balance:,.2f}"
        )

    with col2:
        st.metric(
            "Account Type",
            ACCOUNT["account_type"]
        )

    with col3:
        st.metric(
            "Transactions",
            len(st.session_state.transactions)
        )

    st.markdown("### 👤 Account Summary")

    c1, c2 = st.columns(2)

    with c1:
        st.write("**Account Holder:**", ACCOUNT["name"])
        st.write("**Account Number:**", ACCOUNT["account_number"])
        st.write("**Customer ID:**", ACCOUNT["customer_id"])
        st.write("**Account Type:**", ACCOUNT["account_type"])

    with c2:
        st.write("**IFSC:**", ACCOUNT["ifsc"])
        st.write("**Branch:**", ACCOUNT["branch"])
        st.write("**Phone:**", ACCOUNT["phone"])
        st.write("**Email:**", ACCOUNT["email"])

    st.markdown("### ⚡ Quick Actions")

    q1, q2, q3, q4 = st.columns(4)

    with q1:
        if st.button("💰 Check Balance"):
            st.session_state.verified = True
            st.info(f"Current demo balance: ₹{st.session_state.balance:,.2f}")

    with q2:
        if st.button("📊 View Transactions"):
            st.info(
                f"You have {len(st.session_state.transactions)} "
                "demo transactions."
            )

    with q3:
        if st.button("📱 UPI"):
            st.info("Go to UPI Payments from the sidebar.")

    with q4:
        if st.button("📞 Support"):
            st.info("Customer Support is available from the sidebar.")


# ============================================================
# ACCOUNT DETAILS
# ============================================================

elif menu == "👤 Account Details":

    st.markdown(
        '<div class="section-title">👤 Account Details</div>',
        unsafe_allow_html=True
    )

    if require_verification():

        st.success("✅ Demo account verified.")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### Personal Information")

            st.write("**Account Holder:**", ACCOUNT["name"])
            st.write("**Customer ID:**", ACCOUNT["customer_id"])
            st.write("**Registered Phone:**", ACCOUNT["phone"])
            st.write("**Registered Email:**", ACCOUNT["email"])

        with col2:

            st.markdown("### Account Information")

            st.write(
                "**Account Number:**",
                ACCOUNT["account_number"]
            )

            st.write(
                "**Account Type:**",
                ACCOUNT["account_type"]
            )

            st.write(
                "**Branch:**",
                ACCOUNT["branch"]
            )

            st.write(
                "**IFSC Code:**",
                ACCOUNT["ifsc"]
            )


# ============================================================
# BALANCE
# ============================================================

elif menu == "💰 Balance":

    st.markdown(
        '<div class="section-title">💰 Account Balance</div>',
        unsafe_allow_html=True
    )

    if require_verification():

        st.markdown(
            f"""
            <div class="balance-card">
                <div>Available Balance</div>
                <div class="balance-amount">
                    ₹{st.session_state.balance:,.2f}
                </div>
                <div>{ACCOUNT["account_type"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(
            "This balance belongs to the fictional demo account only."
        )


# ============================================================
# TRANSACTIONS
# ============================================================

elif menu == "📊 Transactions":

    st.markdown(
        '<div class="section-title">📊 Transaction History</div>',
        unsafe_allow_html=True
    )

    if require_verification():

        st.write("### Recent Transactions")

        for transaction in st.session_state.transactions:

            if transaction["type"] == "Credit":
                icon = "🟢"
            else:
                icon = "🔴"

            col1, col2, col3 = st.columns([2, 1, 1])

            with col1:
                st.write(
                    f"{icon} **{transaction['description']}**"
                )
                st.caption(transaction["date"])

            with col2:
                st.write(transaction["type"])

            with col3:

                if transaction["type"] == "Credit":
                    st.write(
                        f"**+ ₹{transaction['amount']:,.2f}**"
                    )
                else:
                    st.write(
                        f"**- ₹{transaction['amount']:,.2f}**"
                    )

            st.divider()


# ============================================================
# UPI PAYMENTS
# ============================================================

elif menu == "📱 UPI Payments":

    st.markdown(
        '<div class="section-title">📱 UPI Payments</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Demo UPI service — no real payment will be made."
    )

    upi_id = st.text_input(
        "Enter Demo UPI ID",
        placeholder="example@upi"
    )

    upi_amount = st.number_input(
        "Enter Amount",
        min_value=1.0,
        max_value=100000.0,
        value=500.0,
        step=100.0
    )

    if st.button("📤 Send Demo UPI Payment", type="primary"):

        if not upi_id:
            st.error("Please enter a UPI ID.")

        elif upi_amount > st.session_state.balance:
            st.error("Insufficient demo balance.")

        else:
            st.session_state.balance -= upi_amount

            add_transaction(
                f"UPI Payment to {upi_id}",
                "Debit",
                upi_amount
            )

            st.success(
                f"✅ Demo UPI payment of ₹{upi_amount:,.2f} "
                f"to {upi_id} completed."
            )


# ============================================================
# MONEY TRANSFER
# ============================================================

elif menu == "💸 Money Transfer":

    st.markdown(
        '<div class="section-title">💸 Money Transfer</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Demo transfer only. No actual bank transfer is performed."
    )

    recipient_name = st.text_input(
        "Recipient Name"
    )

    recipient_account = st.text_input(
        "Recipient Demo Account Number"
    )

    amount = st.number_input(
        "Transfer Amount",
        min_value=1.0,
        max_value=100000.0,
        value=1000.0,
        step=100.0
    )

    if st.button("💸 Transfer Demo Money", type="primary"):

        if not recipient_name:
            st.error("Please enter recipient name.")

        elif not recipient_account:
            st.error("Please enter recipient account number.")

        elif amount > st.session_state.balance:
            st.error("Insufficient demo balance.")

        else:

            st.session_state.balance -= amount

            add_transaction(
                f"Transfer to {recipient_name}",
                "Debit",
                amount
            )

            st.success(
                f"✅ Demo transfer of ₹{amount:,.2f} "
                f"to {recipient_name} completed."
            )


# ============================================================
# CARDS
# ============================================================

elif menu == "💳 Cards":

    st.markdown(
        '<div class="section-title">💳 Card Services</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h3>💳 Demo Debit Card</h3>
        <p><b>Card Holder:</b> CHIYA</p>
        <p><b>Card Number:</b> XXXX XXXX XXXX 1234</p>
        <p><b>Expiry:</b> XX/XX</p>
        <p><b>CVV:</b> XXX</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("🔒 Block Card"):
            st.warning("Demo card has been blocked.")

    with c2:
        if st.button("🔓 Unblock Card"):
            st.success("Demo card has been unblocked.")

    with c3:
        if st.button("📋 Card Details"):
            st.info("Only masked demo card details are displayed.")


# ============================================================
# ATM SERVICES
# ============================================================

elif menu == "🏧 ATM Services":

    st.markdown(
        '<div class="section-title">🏧 ATM Services</div>',
        unsafe_allow_html=True
    )

    st.info(
        "This is a simulated ATM service for demonstration."
    )

    atm_action = st.selectbox(
        "Select ATM Service",
        [
            "Check Balance",
            "Cash Withdrawal",
            "Cash Deposit",
            "Generate ATM PIN"
        ]
    )

    if atm_action == "Check Balance":

        if st.button("💰 Show ATM Balance"):
            st.success(
                f"Demo balance: ₹{st.session_state.balance:,.2f}"
            )

    elif atm_action == "Cash Withdrawal":

        withdrawal = st.number_input(
            "Withdrawal Amount",
            min_value=100.0,
            max_value=50000.0,
            value=1000.0,
            step=100.0
        )

        if st.button("🏧 Withdraw Demo Cash"):

            if withdrawal > st.session_state.balance:
                st.error("Insufficient demo balance.")

            else:

                st.session_state.balance -= withdrawal

                add_transaction(
                    "ATM Cash Withdrawal",
                    "Debit",
                    withdrawal
                )

                st.success(
                    f"₹{withdrawal:,.2f} demo cash withdrawal successful."
                )

    elif atm_action == "Cash Deposit":

        deposit = st.number_input(
            "Deposit Amount",
            min_value=100.0,
            max_value=100000.0,
            value=1000.0,
            step=100.0
        )

        if st.button("💵 Deposit Demo Cash"):

            st.session_state.balance += deposit

            add_transaction(
                "ATM Cash Deposit",
                "Credit",
                deposit
            )

            st.success(
                f"₹{deposit:,.2f} demo cash deposit successful."
            )

    elif atm_action == "Generate ATM PIN":

        if st.button("🔢 Generate Demo PIN"):

            st.info(
                "Demo PIN generated: ****\n\n"
                "For security, real banking applications "
                "should never display PINs like this."
            )


# ============================================================
# LOANS
# ============================================================

elif menu == "🏦 Loans":

    st.markdown(
        '<div class="section-title">🏦 Loan Services</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Loan information shown below is only for demonstration."
    )

    loan_type = st.selectbox(
        "Select Loan Type",
        [
            "Education Loan",
            "Personal Loan",
            "Home Loan",
            "Vehicle Loan"
        ]
    )

    loan_amount = st.number_input(
        "Required Loan Amount",
        min_value=10000.0,
        max_value=10000000.0,
        value=100000.0,
        step=10000.0
    )

    if st.button("📋 Check Demo Loan Details"):

        st.success(
            f"Selected: {loan_type}\n\n"
            f"Requested amount: ₹{loan_amount:,.2f}"
        )

        st.write("### Example Information")

        st.write("• Interest rate: Demo value")
        st.write("• Tenure: Demo value")
        st.write("• Processing fee: Demo value")
        st.write("• Eligibility: Subject to bank rules")


# ============================================================
# DEPOSITS
# ============================================================

elif menu == "💵 Deposits":

    st.markdown(
        '<div class="section-title">💵 Deposit Services</div>',
        unsafe_allow_html=True
    )

    deposit_type = st.selectbox(
        "Select Deposit",
        [
            "Fixed Deposit",
            "Recurring Deposit",
            "Savings Deposit"
        ]
    )

    amount = st.number_input(
        "Deposit Amount",
        min_value=1000.0,
        max_value=10000000.0,
        value=10000.0,
        step=1000.0
    )

    if st.button("💵 Create Demo Deposit"):

        st.success(
            f"Demo {deposit_type} created for "
            f"₹{amount:,.2f}."
        )

        st.info(
            "No real deposit has been created."
        )


# ============================================================
# SECURITY
# ============================================================

elif menu == "🔐 Security":

    st.markdown(
        '<div class="section-title">🔐 Security Center</div>',
        unsafe_allow_html=True
    )

    st.success("🟢 Demo account security status: Active")

    security_options = [
        "Change Password",
        "Enable Two-Factor Authentication",
        "View Login Activity",
        "Report Suspicious Activity"
    ]

    selected_security = st.selectbox(
        "Security Service",
        security_options
    )

    if selected_security == "Change Password":

        st.text_input(
            "New Password",
            type="password"
        )

        if st.button("🔑 Update Demo Password"):
            st.success(
                "Demo password update simulated successfully."
            )

    elif selected_security == "Enable Two-Factor Authentication":

        if st.button("🛡️ Enable 2FA"):

            st.success(
                "Demo Two-Factor Authentication enabled."
            )

    elif selected_security == "View Login Activity":

        st.write("### Recent Demo Login")

        st.write("Device: Demo Windows Device")
        st.write("Location: Demo Location")
        st.write("Status: Successful")

    else:

        message = st.text_area(
            "Describe the suspicious activity"
        )

        if st.button("🚨 Submit Demo Report"):

            if message:
                st.success(
                    "Demo security report submitted."
                )
            else:
                st.error(
                    "Please enter a description."
                )


# ============================================================
# IFSC
# ============================================================

elif menu == "🏢 IFSC":

    st.markdown(
        '<div class="section-title">🏢 IFSC Information</div>',
        unsafe_allow_html=True
    )

    st.write("### Demo Branch Information")

    st.write("**Bank:** Demo Bank")
    st.write("**Branch:**", ACCOUNT["branch"])
    st.write("**IFSC Code:**", ACCOUNT["ifsc"])
    st.write("**City:** Demo City")
    st.write("**State:** Karnataka")

    search_ifsc = st.text_input(
        "Enter IFSC to search",
        placeholder="DEMO0001234"
    )

    if st.button("🔎 Search IFSC"):

        if search_ifsc.upper() == ACCOUNT["ifsc"]:
            st.success(
                f"IFSC found: {ACCOUNT['ifsc']}"
            )
        else:
            st.warning(
                "No matching demo IFSC found."
            )


# ============================================================
# CUSTOMER SUPPORT
# ============================================================

elif menu == "📞 Customer Support":

    st.markdown(
        '<div class="section-title">📞 Customer Support</div>',
        unsafe_allow_html=True
    )

    st.info(
        "This is a demo support center."
    )

    support_topic = st.selectbox(
        "Choose a topic",
        [
            "Account",
            "UPI",
            "Cards",
            "ATM",
            "Loans",
            "Transactions",
            "Security"
        ]
    )

    st.write(
        f"### Support: {support_topic}"
    )

    support_message = st.text_area(
        "Describe your question"
    )

    if st.button("📨 Submit Support Request"):

        if support_message:

            st.success(
                "Your demo support request has been submitted."
            )

        else:

            st.warning(
                "Please describe your question."
            )

    st.markdown("### 📞 Demo Contact")

    st.write("Customer Care: 1800-XXX-XXXX")
    st.write("Email: support@demobank.example")


# ============================================================
# AI CHATBOT
# ============================================================

elif menu == "🤖 AI Chatbot":

    st.markdown(
        '<div class="section-title">🤖 AI Banking Assistant</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Ask questions about your demo account, balance, "
        "transactions, UPI, cards, ATM, loans, deposits, "
        "IFSC or security."
    )

    # Display previous messages

    for message in st.session_state.chat_messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_message = st.chat_input(
        "Ask your banking question..."
    )

    if user_message:

        st.session_state.chat_messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        text = user_message.lower()

        response = ""

        # --------------------------------------------
        # GREETING
        # --------------------------------------------

        if any(
            word in text
            for word in [
                "hello",
                "hi",
                "hey",
                "hii"
            ]
        ):

            response = (
                "👋 Hello Chiya! Welcome to the "
                "AI Banking Assistant.\n\n"
                "How can I help you today?"
            )

        # --------------------------------------------
        # BALANCE
        # --------------------------------------------

        elif (
            "balance" in text
            or "how much money" in text
        ):

            if st.session_state.verified:

                response = (
                    f"💰 Your current demo balance is "
                    f"₹{st.session_state.balance:,.2f}."
                )

            else:

                response = (
                    "🔐 Please verify your demo account "
                    "using the Account Details section first."
                )

        # --------------------------------------------
        # ACCOUNT DETAILS
        # --------------------------------------------

        elif (
            "account" in text
            or "account details" in text
        ):

            if st.session_state.verified:

                response = (
                    f"👤 **Account Details**\n\n"
                    f"Account Holder: {ACCOUNT['name']}\n\n"
                    f"Account Number: {ACCOUNT['account_number']}\n\n"
                    f"Account Type: {ACCOUNT['account_type']}\n\n"
                    f"IFSC: {ACCOUNT['ifsc']}\n\n"
                    f"Branch: {ACCOUNT['branch']}"
                )

            else:

                response = (
                    "🔐 Please verify the demo account "
                    "before viewing protected account details."
                )

        # --------------------------------------------
        # TRANSACTIONS
        # --------------------------------------------

        elif (
            "transaction" in text
            or "transactions" in text
            or "history" in text
        ):

            if st.session_state.verified:

                latest = st.session_state.transactions[:5]

                response = "📊 **Recent Demo Transactions**\n\n"

                for transaction in latest:

                    sign = (
                        "+"
                        if transaction["type"] == "Credit"
                        else "-"
                    )

                    response += (
                        f"• {transaction['description']} — "
                        f"{sign}₹{transaction['amount']:,.2f}\n"
                    )

            else:

                response = (
                    "🔐 Please verify your demo account "
                    "to view transactions."
                )

        # --------------------------------------------
        # ACCOUNT HOLDER
        # --------------------------------------------

        elif (
            "holder" in text
            or "my name" in text
            or "account name" in text
        ):

            response = (
                f"👤 The demo account holder is "
                f"**{ACCOUNT['name']}**."
            )

        # --------------------------------------------
        # UPI
        # --------------------------------------------

        elif "upi" in text:

            response = (
                "📱 **UPI Payments**\n\n"
                "You can use the UPI Payments section "
                "to simulate a demo UPI payment."
            )

        # --------------------------------------------
        # CARD
        # --------------------------------------------

        elif (
            "card" in text
            or "debit card" in text
        ):

            response = (
                "💳 **Card Services**\n\n"
                "You can view your masked demo card, "
                "block it or unblock it from the Cards section."
            )

        # --------------------------------------------
        # ATM
        # --------------------------------------------

        elif "atm" in text:

            response = (
                "🏧 **ATM Services**\n\n"
                "The demo ATM supports simulated balance "
                "checking, deposits and withdrawals."
            )

        # --------------------------------------------
        # LOAN
        # --------------------------------------------

        elif "loan" in text:

            response = (
                "🏦 **Loans**\n\n"
                "The demo application provides example "
                "options for education, personal, home "
                "and vehicle loans."
            )

        # --------------------------------------------
        # DEPOSIT
        # --------------------------------------------

        elif "deposit" in text:

            response = (
                "💵 **Deposits**\n\n"
                "You can explore demo Fixed Deposit, "
                "Recurring Deposit and Savings Deposit options."
            )

        # --------------------------------------------
        # IFSC
        # --------------------------------------------

        elif "ifsc" in text:

            response = (
                f"🏢 Demo IFSC Code: **{ACCOUNT['ifsc']}**\n\n"
                f"Branch: **{ACCOUNT['branch']}**"
            )

        # --------------------------------------------
        # SECURITY
        # --------------------------------------------

        elif (
            "security" in text
            or "otp" in text
            or "password" in text
        ):

            response = (
                "🔐 **Security Tips**\n\n"
                "• Never share your OTP.\n"
                "• Never share your password or PIN.\n"
                "• Use strong passwords.\n"
                "• Report suspicious activity to your bank."
            )

        # --------------------------------------------
        # SUPPORT
        # --------------------------------------------

        elif (
            "help" in text
            or "support" in text
        ):

            response = (
                "📞 I can help you with:\n\n"
                "• Account Details\n"
                "• Balance\n"
                "• Transactions\n"
                "• UPI\n"
                "• Money Transfer\n"
                "• Cards\n"
                "• ATM\n"
                "• Loans\n"
                "• Deposits\n"
                "• Security\n"
                "• IFSC"
            )

        # --------------------------------------------
        # THANKS
        # --------------------------------------------

        elif (
            "thank" in text
            or "thanks" in text
        ):

            response = (
                "You're welcome! 😊 "
                "I'm always happy to help."
            )

        # --------------------------------------------
        # UNKNOWN
        # --------------------------------------------

        else:

            response = (
                "🤖 I can help with banking topics such as:\n\n"
                "💰 Balance\n"
                "👤 Account Details\n"
                "📊 Transactions\n"
                "📱 UPI\n"
                "💸 Money Transfer\n"
                "💳 Cards\n"
                "🏧 ATM\n"
                "🏦 Loans\n"
                "💵 Deposits\n"
                "🔐 Security\n"
                "🏢 IFSC\n\n"
                "Try asking: **What is my balance?**"
            )

        st.session_state.chat_messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "🏦 AI Banking Assistant • Educational Demo • "
    "All account information and transactions are fictional."
)