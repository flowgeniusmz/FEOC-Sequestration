import streamlit as st
from  functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview
from functions.supabase import get_data_notifications



st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    set_title("FEOC", "Central Performance Panel")
    set_page_overview("Main Header", "View key information and metrics related to your FEOC.")
    dfAlerts = get_data_notifications()
    st.progress(.5, "Total Emissions Reduced")
    st.divider()
    main_container = st.container()
    with main_container:
        st.markdown("#### Notifications and Alerts")
        exp0 = st.expander("", expanded=True)
        with exp0:
            dfAlert = st.dataframe(dfAlerts, use_container_width=True, column_config = {
                ")
        st.markdown("#### Certificate Information")
        exp1 = st.expander("", expanded=True)
        with exp1:
            col11, col12 = st.columns(2)
            with col11:
                st.markdown("**Details**")
                col111, col112, col113, col114 = st.columns(4)
                with col111:
                  st.markdown("Project")
                  st.markdown("FEOC ID")
                  st.markdown("Start Date")
                  st.markdown("End Date")
                with col112:
                  st.markdown("Carbon Offset for Refinery")
                  st.markdown("FEOC-001")
                  st.markdown("01/01/2023")
                  st.markdown("12/31/2023")
                with col111:
                  st.markdown("Emitter")
                  st.markdown("Provider")
                  st.markdown("Purchaser")
                  st.markdown("AAA Rating")
                with col114:
                  st.markdown("Bevron Refinery")
                  st.markdown("Wizmo Power")
                  st.markdown("Welta Airlines")
                  st.markdown("A")

    # Define your dynamic variables
    operational_profits = 400000
    total_net_zero_fuel_sold = 1000000
    total_net_zero_tickets_sold = 10000000
    current_oc_value = 2504543232
    
    annual_offset_committed = 400000
    annual_offset_actual = 300000
    annual_offset_variance = annual_offset_committed - annual_offset_actual
    
    validation_date = "9/21/2023"
    validation_message = "Please check data compliance"
    success_date = "9/20/2023"
    success_message = "Data validation successfully completed; no errors"
    info_date = "9/15/2023"
    info_message = "Forward-selling activity initiated (100,000 tons fuel)"          
      
    next_container = st.container()
    with next_container:
          exp2 = st.expander("Performance", expanded=True)
          with exp2:
              col21, col22, col23 = st.columns(3)
              with col21:
                st.markdown("#### Financial")
                st.markdown(f"**Operational Profits of Provider:** {operational_profits} metric tons CO₂e")
                st.markdown(f"**Total Net-Zero Fuel Sold:** {total_net_zero_fuel_sold} metric tons")
                st.markdown(f"**Total Net-Zero Tickets Sold:** {total_net_zero_tickets_sold} tickets")
                st.markdown(f"**Current OC Value:** ${current_oc_value}")
            
              with col22:
                st.markdown("#### Carbon Reduction")
                st.markdown(f"**Annual Offset (Committed):** {annual_offset_committed} metric tons CO₂e")
                st.markdown(f"**Annual Offset (Actual):** {annual_offset_actual} metric tons CO₂e")
                st.markdown(f"**Annual Offset (Variance):** {annual_offset_variance} ({annual_offset_variance / annual_offset_committed * 100:.2f}%) metric tons CO₂e")
            
              with col23:
                st.markdown("#### Validation and Verification")
                st.warning(f"{validation_date}: {validation_message}")
                st.success(f"{success_date}: {success_message}")
                st.info(f"{info_date}: {info_message}")
    