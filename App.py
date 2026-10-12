import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="ارشاد سینیٹری مارٹ - انٹپرائز مینجমেন্ট سسٹم", layout="wide"
)

# App Title & Branding
st.title("🚰 ارشاد سینیٹری مارٹ - مکمل انوینٹری و مینجمنٹ سسٹم")
st.markdown("---")

# Initialize Session State Databases with Complete PPRC Catalog & Sizes
if "inventory" not in st.session_state:
  st.session_state["inventory"] = {
      "📦 PPRC سیکشن (مکمل سائز کیٹلاگ)": pd.DataFrame([
          {
              "Item Name": "PPRC Pipe (ਪੀਪੀਆਰਸੀ ਪਾਈਪ) - 20mm",
              "Stock": 25,
              "Cost Price": 280,
              "Sale Price": 380,
          },
          {
              "Item Name": "PPRC Pipe (ਪੀਪੀਆਰਸੀ ਪਾਈਪ) - 25mm",
              "Stock": 30,
              "Cost Price": 400,
              "Sale Price": 520,
          },
          {
              "Item Name": "PPRC Pipe (ਪੀਪੀਆਰਸੀ ਪਾਈਪ) - 32mm",
              "Stock": 20,
              "Cost Price": 650,
              "Sale Price": 850,
          },
          {
              "Item Name": "PPRC Pipe (ਪੀਪੀਆਰਸੀ ਪਾਈਪ) - 40mm",
              "Stock": 15,
              "Cost Price": 1100,
              "Sale Price": 1400,
          },
          {
              "Item Name": "PPRC Pipe (ਪੀਪੀਆਰਸੀ ਪਾਈਪ) - 50mm & 63mm",
              "Stock": 10,
              "Cost Price": 1800,
              "Sale Price": 2300,
          },
          {
              "Item Name": (
                  "Elbow (ایلبو) - 25mm, 32mm, 40mm, 50mm, 63mm"
              ),
              "Stock": 50,
              "Cost Price": 30,
              "Sale Price": 50,
          },
          {
              "Item Name": "TEE (ٹی) - 25mm, 32mm, 40mm, 50mm, 63mm",
              "Stock": 45,
              "Cost Price": 35,
              "Sale Price": 60,
          },
          {
              "Item Name": "Socket (ساکٹ) - 25mm, 32mm, 40mm, 50mm, 63mm",
              "Stock": 40,
              "Cost Price": 25,
              "Sale Price": 40,
          },
          {
              "Item Name": (
                  "Female Elbow (فی میل ایلبو) - 25 x 1/2\", 25 x 3/4\", 32 x"
                  ' 1/2", 32 x 3/4", 32 x 1", 40 x 1 1/4"'
              ),
              "Stock": 25,
              "Cost Price": 150,
              "Sale Price": 220,
          },
          {
              "Item Name": (
                  "Female Tee (فی میل ٹی) - 25 x 1/2\", 25 x 3/4\", 32 x 1/2\","
                  ' 32 x 3/4", 32 x 1", 40 x 1 1/4"'
              ),
              "Stock": 20,
              "Cost Price": 180,
              "Sale Price": 260,
          },
          {
              "Item Name": (
                  "Female Socket (فی میل ساکٹ) - 25 x 1/2\", 25 x 3/4\", 32 x"
                  ' 1/2", 32 x 3/4", 32 x 1", 40 x 1 1/4", 50 x 1 1/2", 63 x'
                  ' 2"'
              ),
              "Stock": 22,
              "Cost Price": 140,
              "Sale Price": 200,
          },
          {
              "Item Name": (
                  "Male Elbow (میل ایلبو) - 25 x 1/2\", 25 x 3/4\", 32 x 1/2\","
                  ' 32 x 3/4", 32 x 1", 40 x 1 1/4"'
              ),
              "Stock": 18,
              "Cost Price": 160,
              "Sale Price": 230,
          },
          {
              "Item Name": (
                  "Male Tee (میل ٹی) - 25 x 1/2\", 25 x 3/4\", 32 x 1/2\", 32"
                  ' x 3/4", 32 x 1", 40 x 1 1/4"'
              ),
              "Stock": 15,
              "Cost Price": 190,
              "Sale Price": 270,
          },
          {
              "Item Name": (
                  "Male Socket (میل ساکٹ) - 25 x 1/2\", 25 x 3/4\", 32 x 1/2\","
                  ' 32 x 3/4", 32 x 1", 40 x 1 1/4", 50 x 1 1/2", 63 x 2"'
              ),
              "Stock": 16,
              "Cost Price": 150,
              "Sale Price": 210,
          },
          {
              "Item Name": (
                  "Reducing Elbow (ریڈیوسنگ ایلبو) - 25 x 32mm, 25 x 40mm, 32 x"
                  " 40mm"
              ),
              "Stock": 12,
              "Cost Price": 70,
              "Sale Price": 110,
          },
          {
              "Item Name": (
                  "Reducing Tee (ریڈیوسنگ ٹی) - 25 x 1/2\", 25 x 3/4\", 32 x"
                  ' 1/2", 32 x 3/4", 32 x 1", 40 x 1 1/4"'
              ),
              "Stock": 14,
              "Cost Price": 80,
              "Sale Price": 120,
          },
          {
              "Item Name": (
                  "Reducing Socket (ریڈیوسنگ ساکٹ) - 25 x 1/2\", 25 x 3/4\","
                  ' 32 x 1/2", 32 x 3/4", 32 x 1", 40 x 1 1/4", 50 x 1 1/2",'
                  ' 63 x 2"'
              ),
              "Stock": 15,
              "Cost Price": 60,
              "Sale Price": 95,
          },
          {
              "Item Name": "Mixer Elbow (مکسر ایلبو) - 25mm",
              "Stock": 10,
              "Cost Price": 350,
              "Sale Price": 500,
          },
          {
              "Item Name": (
                  "Gate Valve (گیٹ والو) - 25mm, 32mm, 40mm, 50mm, 63mm"
              ),
              "Stock": 8,
              "Cost Price": 450,
              "Sale Price": 650,
          },
          {
              "Item Name": "Plug (پلگ) - 20mm (1/2\"), 25mm (3/4\"), 32mm (1\")",
              "Stock": 30,
              "Cost Price": 20,
              "Sale Price": 35,
          },
          {
              "Item Name": "End Cap (اینڈ کیپ) - 25mm, 32mm",
              "Stock": 25,
              "Cost Price": 25,
              "Sale Price": 40,
          },
          {
              "Item Name": "Clamp (کلیمپ) - 25mm, 32mm",
              "Stock": 50,
              "Cost Price": 15,
              "Sale Price": 25,
          },
          {
              "Item Name": "Nail Clamp (نیل کلیمپ) - 25mm, 32mm",
              "Stock": 60,
              "Cost Price": 10,
              "Sale Price": 20,
          },
          {
              "Item Name": "Over Cross (اوور کراس) - 25mm, 32mm, 40mm",
              "Stock": 12,
              "Cost Price": 90,
              "Sale Price": 140,
          },
          {
              "Item Name": "UNION (یونین) - 25mm, 32mm, 40mm",
              "Stock": 10,
              "Cost Price": 250,
              "Sale Price": 360,
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
      ]),
      "🟡 براس آئٹمز (Brass Items)": pd.DataFrame([
          {
              "Item Name": "Brass Bibcock (براس بب کاک)",
              "Stock": 18,
              "Cost Price": 1200,
              "Sale Price": 1500,
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
      ]),
      "⚪ اسٹیل آئٹمز (Steel Items)": pd.DataFrame([
          {
              "Item Name": "Steel Bibcock (اسٹیل بب کاک)",
              "Stock": 14,
              "Cost Price": 900,
              "Sale Price": 1300,
          },
      ]),
      "🚿 واش بیسن اور فٹنگز": pd.DataFrame([
          {
              "Item Name": "Wash Basin Set Complete",
              "Stock": 8,
              "Cost Price": 2500,
              "Sale Price": 3400,
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
    "📦 PPRC سیکشن (مکمل سائز کیٹلاگ)",
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
      item_name = st.text_input("آئٹم کا نام اور سائز")
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

    submit_sale = st.form_submit_button("فروخت درج کریں اور منافع محاسبه کریں")

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
      io_item = st.text_input("آئٹم کا نام اور سائز")
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

# 4. Inventory Sections
else:
  st.subheader(f"انوینٹری اسٹاک - {menu}")
  st.markdown(
      "آپ یہاں تمام فٹنگز اور ان کے سائز دیکھ سکتے ہیں اور براہِ راست **Stock"
      " (تعداد)** تبدیل کر سکتے ہیں!"
  )

  df = st.session_state["inventory"][menu]
  edited_df = st.data_editor(
      df, num_rows="dynamic", use_container_width=True, key=f"editor_{menu}"
  )

  edited_df["Total Value"] = edited_df["Stock"] * edited_df["Cost Price"]
  st.session_state["inventory"][menu] = edited_df

  low_stock_filter = edited_df[edited_df["Stock"] < 5]
  if not low_stock_filter.empty:
    st.warning("⚠️ انتباہ: اس سیکشن میں مندرجہ ذیل آئٹمز کی مقدار 5 سے کم ہے:")
    st.dataframe(
        low_stock_filter[["Item Name", "Stock", "Sale Price"]],
        use_container_width=True,
              )
        
