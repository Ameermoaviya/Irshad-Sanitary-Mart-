import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ارشاد سینیٹری مارٹ - پروفیشنل سافٹ ویئر", layout="wide"
)

# App Title & Branding
fn_title = "🚰 ارشاد سینیٹری مارٹ - انٹرپرائز مینجمنٹ سسٹم"
st.title(fn_title)
st.markdown(
    "---"
)  # Enterprise-grade management for PPRC, PVC, Brass, Plastic, and Steel items.

# Initialize Session State Databases
if "inventory" not in st.session_state:
  st.session_state["inventory"] = {
      "📦 PPRC سیکشن": pd.DataFrame([
          {
              "Item Name": "PPRC Pipe 20mm (1/2\")",
              "Stock": 25,
              "Cost Price": 300,
              "Sale Price": 400,
          },
          {
              "Item Name": "PPRC Pipe 25mm (3/4\")",
              "Stock": 20,
              "Cost Price": 420,
              "Sale Price": 550,
          },
          {
              "Item Name": "PPRC Elbow 20mm",
              "Stock": 40,
              "Cost Price": 25,
              "Sale Price": 40,
          },
          {
              "Item Name": "PPRC Tee 20mm",
              "Stock": 35,
              "Cost Price": 30,
              "Sale Price": 50,
          },
          {
              "Item Name": "PPRC Socket 20mm",
              "Stock": 30,
              "Cost Price": 20,
              "Sale Price": 35,
          },
          {
              "Item Name": "PPRC Ball Valve 20mm",
              "Stock": 12,
              "Cost Price": 450,
              "Sale Price": 650,
          },
      ]),
      "🚰 PVC سیکشن": pd.DataFrame([
          {
              "Item Name": "PVC Pipe 1 inch",
              "Stock": 15,
              "Cost Price": 450,
              "Sale Price": 600,
          },
          {
              "Item Name": "PVC Pipe 2 inch",
              "Stock": 10,
              "Cost Price": 850,
              "Sale Price": 1100,
          },
          {
              "Item Name": "PVC Elbow 1 inch",
              "Stock": 3,
              "Cost Price": 30,
              "Sale Price": 50,
          },
          {
              "Item Name": "PVC Socket 1 inch",
              "Stock": 4,
              "Cost Price": 40,
              "Sale Price": 65,
          },
          {
              "Item Name": "PVC Tee 1 inch",
              "Stock": 12,
              "Cost Price": 45,
              "Sale Price": 70,
          },
      ]),
      "🟡 براس آئٹمز (Brass Items)": pd.DataFrame([
          {
              "Item Name": "Brass Bibcock (براس بب کاک)",
              "Stock": 18,
              "Cost Price": 1200,
              "Sale Price": 1500,
          },
          {
              "Item Name": "Brass T-Cock",
              "Stock": 10,
              "Cost Price": 850,
              "Sale Price": 1200,
          },
          {
              "Item Name": "Brass Stop Cock",
              "Stock": 11,
              "Cost Price": 950,
              "Sale Price": 1350,
          },
      ]),
      "🟢 پلاسٹک آئٹمز (Plastic Items)": pd.DataFrame([
          {
              "Item Name": "Plastic Bibcock (پلاسٹک بب کاک)",
              "Stock": 2,
              "Cost Price": 150,
              "Sale Price": 220,
          },
          {
              "Item Name": "Plastic T-Cock",
              "Stock": 15,
              "Cost Price": 250,
              "Sale Price": 380,
          },
      ]),
      "⚪ اسٹیل آئٹمز (Steel Items)": pd.DataFrame([
          {
              "Item Name": "Steel Bibcock (اسٹیل بب کاک)",
              "Stock": 14,
              "Cost Price": 900,
              "Sale Price": 1300,
          },
          {
              "Item Name": "Steel Floor Waste",
              "Stock": 7,
              "Cost Price": 350,
              "Sale Price": 500,
          },
      ]),
      "🚿 واش بیسن اور فٹنگز": pd.DataFrame([
          {
              "Item Name": "Wash Basin Set Complete",
              "Stock": 8,
              "Cost Price": 2500,
              "Sale Price": 3400,
          },
          {
              "Item Name": "Basin Waste Pipe",
              "Stock": 12,
              "Cost Price": 120,
              "Sale Price": 180,
          },
          {
              "Item Name": "Sink Waste",
              "Stock": 10,
              "Cost Price": 150,
              "Sale Price": 230,
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

if "stock_ledger" not in st.session_state:
  st.session_state["stock_ledger"] = pd.DataFrame(
      columns=["Date", "Item Name", "Type (In/Out)", "Quantity", "Remarks"]
  )

# Sidebar Navigation Menu
menu = st.sidebar.selectbox("مینو منتخب کریں (Menu)", [
    "📊 ایگزیکٹو ڈیش بورڈ (Dashboard)",
    "💰 ڈیلی سیل اور پرافٹ انٹری (Daily Sales & Profit)",
    "📥 اسٹاک ان / آؤট لیجر (Stock In/Out)",
    "📦 PPRC سیکشن",
    "🚰 PVC سیکشن",
    "🟡 براس آئٹمز (Brass Items)",
    "🟢 پلاسٹک آئٹمز (Plastic Items)",
    "⚪ اسٹیل آئٹمز (Steel Items)",
    "🚿 واش بیسن اور فٹنگز",
])

# 1. Executive Dashboard
if menu == "📊 ایگزیکٹو ڈیش بورڈ (Dashboard)":
  st.subheader("ارشاد سینیٹری مارٹ - فنانشل اور اسٹاک ڈیش بورڈ")

  total_stock_value = 0
  low_stock_items = []

  for cat, df in st.session_state["inventory"].items():
    df["Total Value"] = df["Stock"] * df["Cost Price"]
    total_stock_value += df["Total Value"].sum()
    low_stock = df[df["Stock"] < 5]
    for idx, row in low_stock.iterrows():
      low_stock_items.append({
          "Category": cat,
          "Item Name": row["Item Name"],
          "Stock": row["Stock"],
      })

  # Calculate Sales & Profit
  total_revenue = (
      st.session_state["sales_history"]["Total Amount"].sum()
      if not st.session_state["sales_history"].empty
      else 0
  )
  total_net_profit = (
      st.session_state["sales_history"]["Profit"].sum()
      if not st.session_state["sales_history"].empty
      else 0
  )

  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.metric(
        label="کل اسٹاک مالیت (Inventory Value)",
        value=f"Rs {total_stock_value:,.2f}",
    )
  with col2:
    st.metric(
        label="کل فروخت (Total Revenue)", value=f"Rs {total_revenue:,.2f}"
    )
  with col3:
    st.metric(
        label="کل صاف منافع (Net Profit)", value=f"Rs {total_net_profit:,.2f}"
    )
  with col4:
    st.metric(label="کم اسٹاک الرٹ (< 5)", value=len(low_stock_items))

  st.markdown("### ⚠️ فوری توجہ طلب: کم اسٹاک آئٹمز (تعداد 5 سے کم)")
  if low_stock_items:
    st.dataframe(pd.DataFrame(low_stock_items), use_container_width=True)
  else:
    st.success("زبردست! تمام آئٹمز کا اسٹاک پورا ہے۔")

# 2. Daily Sales & Profit Entry
elif menu == "💰 ڈیلی سیل اور پرافٹ انٹری (Daily Sales & Profit)":
  st.subheader("روزمرہ کی سیل اور آٹو پرافٹ کیلکولیٹر")

  with st.form("sales_form"):
    col1, col2 = st.columns(2)
    with col1:
      item_name = st.text_input(
          "آئٹم کا نام (مثلاً: Brass Bibcock یا PPRC Elbow 20mm)"
      )
      qty_sold = st.number_input(
          "فروخت ہونے والی تعداد (Quantity)", min_value=1, value=1
      )
    with col2:
      cost_p = st.number_input(
          "فی یونٹ خریدی قیمت (Cost Price)", min_value=0.0, value=0.0
      )
      sale_p = st.number_input(
          "فی یونٹ فروخت قیمت (Selling Price)", min_value=0.0, value=0.0
      )

    submit_sale = st.form_submit_button(
        "فروخت درج کریں اور منافع محاسبه کریں (Submit Sale)"
    )

    if submit_sale and item_name:
      total_amt = qty_sold * sale_p
      profit = qty_sold * (sale_p - cost_p)

      new_sale = pd.DataFrame([{
          "Date": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"),
          "Item Name": item_name,
          "Quantity Sold": qty_sold,
          "Sale Price": sale_p,
          "Total Amount": total_amt,
          "Profit": profit,
      }])
      st.session_state["sales_history"] = pd.concat(
          [st.session_state["sales_history"], new_sale], ignore_index=True
      )
      st.success(
          f" کامیابی سے سیل درج ہو گئی! کل رقم: Rs {total_amt:,.2f} | خالص منافع:"
          f" Rs {profit:,.2f}"
      )

  st.markdown("### 📜 تمام سیل اور پرافٹ کا ریکارڈ:")
  st.dataframe(st.session_state["sales_history"], use_container_width=True)

# 3. Stock In/Out Ledger
elif menu == "📥 اسٹاک ان / آؤট لیجر (Stock In/Out)":
  st.subheader("روزانہ نیا مال آنے (In) اور جانے (Out) کا ریکارڈ")

  with st.form("stock_inout_form"):
    col1, col2 = st.columns(2)
    with col1:
      io_item = st.text_input("آئٹم کا نام")
      io_type = st.selectbox(
          "عمل کی نوعیت (Type)", ["نیا مال خریدا (Stock IN)", "مال باہر گیا (Stock OUT)"]
      )
    with col2:
      io_qty = st.number_input("تعداد (Quantity)", min_value=1, value=1)
      io_remarks = st.text_input("تفصیل / سپلائر کا نام (Remarks)")

    submit_io = st.form_submit_button("اسٹاک لیجر میں درج کریں")

    if submit_io and io_item:
      new_ledger = pd.DataFrame([{
          "Date": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"),
          "Item Name": io_item,
          "Type (In/Out)": io_type,
          "Quantity": io_qty,
          "Remarks": io_remarks,
      }])
      st.session_state["stock_ledger"] = pd.concat(
          [st.session_state["stock_ledger"], new_ledger], ignore_index=True
      )
      st.success("اسٹاک ریکارڈ کامیابی سے اپ ڈیٹ ہو گیا!")

  st.markdown("### 📋 اسٹاک ان/آؤٹ ہسٹری:")
  st.dataframe(st.session_state["stock_ledger"], use_container_width=True)

# 4. Inventory Sections (PPRC, PVC, Brass, Plastic, Steel, Wash Basin)
elif menu in [
    "📦 PPRC سیکشن",
    "🚰 PVC سیکشن",
    "🟡 براس آئٹمز (Brass Items)",
    "🟢 پلاسٹک آئٹمز (Plastic Items)",
    "⚪ اسٹیل آئٹمز (Steel Items)",
    "🚿 واش بیسن اور فٹنگز",
]:
  st.subheader(f"انوینٹری اسٹاک - {menu}")
  st.markdown(
      "آپ یہاں براہِ راست **Stock (تعداد)** تبدیل کریں، کل مالیت خود بخود"
      " کیلکولیٹ ہو جائے گی!"
  )

  df = st.session_state["inventory"][menu]
  edited_df = st.data_editor(
      df, num_rows="dynamic", use_container_width=True, key=f"editor_{menu}"
  )

  edited_df["Total Value"] = edited_df["Stock"] * edited_df["Cost Price"]
  st.session_state["inventory"][menu] = edited_df

  # Low stock warning check
  low_stock_filter = edited_df[edited_df["Stock"] < 5]
  if not low_stock_filter.empty:
    st.warning("⚠️ انتباہ: اس سیکشن میں مندرجہ ذیل آئٹمز کی مقدار 5 سے کم ہے:")
    st.dataframe(
        low_stock_filter[["Item Name", "Stock", "Sale Price"]],
        use_container_width=True,
            )
  
