import math
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ارشاد سینیٹری مارٹ - انٹپرائز مینجمنٹ سسٹم", layout="wide"
)

# App Title & Branding
st.title("🚰 ارشاد سینیٹری مارٹ - انوینٹری و انوائس سسٹم")
st.markdown("---")

# Initialize Session State
if "inventory" not in st.session_state:
  st.session_state["inventory"] = {
      "📦 PPRC سیکشن (ACCUFIT & Duramax)": pd.DataFrame([
          {
              "Item Name": "ELBOW 32+1/2 ACCUFIT",
              "Stock": 50,
              "Cost Price": 280,
              "Sale Price": 391.0,
          },
          {
              "Item Name": "TEE 25+1/2 ACCUFIT",
              "Stock": 45,
              "Cost Price": 180,
              "Sale Price": 262.0,
          },
          {
              "Item Name": "SOCKET 32MM ACCUFIT",
              "Stock": 60,
              "Cost Price": 25,
              "Sale Price": 37.0,
          },
          {
              "Item Name": "SOCKET 32+1 ACCUFIT",
              "Stock": 30,
              "Cost Price": 400,
              "Sale Price": 560.0,
          },
          {
              "Item Name": "CROSS BEND 25 MM ACCUFIT",
              "Stock": 20,
              "Cost Price": 90,
              "Sale Price": 143.0,
          },
          {
              "Item Name": "PPRC Pipe 25mm",
              "Stock": 30,
              "Cost Price": 400,
              "Sale Price": 520.0,
          },
      ]),
      "🚰 PVC سیکشن": pd.DataFrame([
          {
              "Item Name": "PVC Pipe 1 inch",
              "Stock": 15,
              "Cost Price": 450,
              "Sale Price": 600.0,
          },
          {
              "Item Name": "PVC Pipe 2 inch",
              "Stock": 10,
              "Cost Price": 850,
              "Sale Price": 1100.0,
          },
      ]),
      "🟡 براس آئٹمز (Brass Items)": pd.DataFrame([
          {
              "Item Name": "Brass Bibcock (براس بب کاک)",
              "Stock": 18,
              "Cost Price": 1200,
              "Sale Price": 1500.0,
          },
      ]),
  }

if "sales_history" not in st.session_state:
  st.session_state["sales_history"] = pd.DataFrame(
      columns=[
          "Date",
          "Item Name",
          "Quantity Sold",
          "Sale Price",
          "Total Amount",
          "Profit",
      ]
  )

if "invoice_items" not in st.session_state:
  st.session_state["invoice_items"] = []

# Sidebar Navigation Menu
menu = st.sidebar.selectbox("مینو منتخب کریں (Menu)", [
    "🧾 نئ بل انوائس بنائیں (Sale Invoice)",
    "📊 ایگزیکٹو ڈیش بورڈ (Dashboard)",
    "💰 ڈیلی سیل اور پرافٹ ہسٹری (Sales Log)",
    "📦 PPRC سیکشن (ACCUFIT & Duramax)",
    "🚰 PVC سیکشن",
    "🟡 براس آئٹمز (Brass Items)",
])

# 1. SALE INVOICE GENERATOR (رسید بنانے کا سسٹم)
if menu == "🧾 نئ بل انوائس بنائیں (Sale Invoice)":
  st.subheader("🧾 ارشاد سینیٹری مارٹ - سیل انوائس (Bill Generator)")

  col_cust1, col_cust2, col_cust3 = st.columns(3)
  with col_cust1:
    customer_name = st.text_input(
        "گاہک کا نام (Customer Name)", "IRSHAD SANITARY STORE"
    )
  with col_cust2:
    bill_no = st.text_input("بل نمبر (Sale Bill #)", "S-2032")
  with col_cust3:
    bill_date = st.date_input("تاریخ (Bill Date)")

  st.markdown("---")
  st.markdown("### 🛒 بل میں سامان شامل کریں:")

  # Add Items to Current Invoice
  with st.form("add_item_to_invoice"):
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
      item_selected = st.text_input(
          "آئٹم کا نام اور سائز (مثلاً: TEE 25+1/2 ACCUFIT)"
      )
    with col2:
      item_qty = st.number_input("تعداد (Qty)", min_value=1, value=1)
    with col3:
      item_rate = st.number_input(
          "ریٹ (Rate)", min_value=0.0, value=100.0, step=10.0
      )

    add_btn = st.form_submit_button("آئٹم بل میں شامل کریں")

    if add_btn and item_selected:
      amount = item_qty * item_rate
      st.session_state["invoice_items"].append({
          "Sr #": len(st.session_state["invoice_items"]) + 1,
          "Item Name": item_selected,
          "Qty": item_qty,
          "Rate": item_rate,
          "Amount": amount,
      })
      st.success(f"{item_selected} بل میں شامل ہو گیا!")

  # Invoice Display & Calculations
  if st.session_state["invoice_items"]:
    st.markdown("---")
    st.markdown("### 📋 بل کا پیش نظارہ (Invoice Preview):")

    inv_df = pd.DataFrame(st.session_state["invoice_items"])
    st.dataframe(inv_df, use_container_width=True)

    col_disc1, col_disc2 = st.columns(2)
    with col_disc1:
      discount = st.number_input("ڈسکاؤنٹ (Discount)", min_value=0.0, value=0.0)
    with col_disc2:
      extra_discount = st.number_input(
          "اضافی ڈسکاؤنٹ (Extra Discount)", min_value=0.0, value=0.0
      )

    subtotal = inv_df["Amount"].sum()
    net_total = subtotal - discount - extra_discount

    st.markdown("---")
    # Printable Receipt Section
    st.markdown(f"""
        <div style="border: 2px solid #333; padding: 20px; background-color: #ffffff; color: #000000; font-family: monospace;">
            <h2 style="text-align: center; margin: 0;">IRSHAD SANITARY STORE</h2>
            <p style="text-align: center; margin: 5px;">Chowk Shahida, Multan | Ph: 0315-2761976</p>
            <h3 style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 5px;">SALE INVOICE</h3>
            <div style="display: flex; justify-content: space-between;">
                <div><b>Sale Bill #:</b> {bill_no}<br><b>Customer:</b> {customer_name}</div>
                <div><b>Bill Date:</b> {bill_date}<br><b>Bill Time:</b> 05:15:00 PM</div>
            </div>
            <br>
            <table style="width: 100%; border-collapse: collapse; text-align: left; color: #000;">
                <thead>
                    <tr style="border-bottom: 1px solid #000;">
                        <th>Sr #</th><th>Item Name</th><th>Qty</th><th>Rate</th><th>Amount</th>
                    </tr>
                </thead>
                <tbody>
                    {"".join([f"<tr><td>{r['Sr #']}</td><td>{r['Item Name']}</td><td>{r['Qty']}</td><td>{r['Rate']:.1f}</td><td>{r['Amount']:.2f}</td></tr>" for r in st.session_state["invoice_items"]])}
                </tbody>
            </table>
            <br>
            <hr style="border: 1px solid #000;">
            <div style="text-align: right;">
                <p><b>Discount :</b> {discount:.2f}</p>
                <p><b>Extra Discount :</b> {extra_discount:.2f}</p>
                <h3><b>Net Total : Rs {net_total:,.2f}</b></h3>
            </div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("بل صاف کریں (Clear Invoice)"):
      st.session_state["invoice_items"] = []
      st.rerun()

# 2. Executive Dashboard
elif menu == "📊 ایگزیکٹو ڈیش بورڈ (Dashboard)":
  st.subheader("ارشاد سینیٹری مارٹ - ڈیش بورڈ")
  total_stock_value = sum(
      (df["Stock"] * df["Cost Price"]).sum()
      for df in st.session_state["inventory"].values()
  )
  st.metric(
      label="کل اسٹاک مالیت (Inventory Value)",
      value=f"Rs {total_stock_value:,.2f}",
  )

# 3. Daily Sales Log
elif menu == "💰 ڈیلی سیل اور پرافٹ ہسٹری (Sales Log)":
  st.subheader("فروخت کا ریکارڈ")
  st.dataframe(st.session_state["sales_history"], use_container_width=True)

# Inventory Pages
else:
  st.subheader(f"انوینٹری - {menu}")
  df = st.session_state["inventory"][menu]
  edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
  st.session_state["inventory"][menu] = edited_df
      
