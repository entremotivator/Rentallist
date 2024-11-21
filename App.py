import streamlit as st

# App Header
st.title("Party Bus & Sprinter Van Listing Directory")
st.subheader("Maximize your reach by listing your services on the best platforms!")

st.markdown(
    """
    This app provides a directory of **25+ platforms** to promote your **party bus** and **sprinter van** services. 
    Use this guide to list your services on high-traffic platforms, event marketplaces, and social media channels. 
    """
)

# Categories for filtering
categories = [
    "General Marketplaces",
    "Event & Wedding Platforms",
    "Transportation Platforms",
    "Social Media Platforms",
    "Local Directories"
]

platforms = [
    {
        "Name": "Yelp",
        "Category": "Local Directories",
        "Description": "Popular for local businesses to attract customers through reviews.",
        "Website": "https://www.yelp.com",
    },
    {
        "Name": "Facebook Marketplace",
        "Category": "Social Media Platforms",
        "Description": "Sell or advertise your services to your local community on Facebook.",
        "Website": "https://www.facebook.com/marketplace",
    },
    {
        "Name": "Craigslist",
        "Category": "General Marketplaces",
        "Description": "Post local ads for your party bus and sprinter van rentals.",
        "Website": "https://www.craigslist.org",
    },
    {
        "Name": "Instagram (Business Account)",
        "Category": "Social Media Platforms",
        "Description": "Promote your services with engaging posts and stories.",
        "Website": "https://www.instagram.com",
    },
    {
        "Name": "Eventbrite",
        "Category": "Event & Wedding Platforms",
        "Description": "Great for marketing event-based services like party buses.",
        "Website": "https://www.eventbrite.com",
    },
    {
        "Name": "Thumbtack",
        "Category": "General Marketplaces",
        "Description": "Connect with customers searching for transportation services.",
        "Website": "https://www.thumbtack.com",
    },
    {
        "Name": "Google My Business",
        "Category": "Local Directories",
        "Description": "Enhance your local visibility with Google Search and Maps.",
        "Website": "https://www.google.com/business/",
    },
    {
        "Name": "Turo",
        "Category": "Transportation Platforms",
        "Description": "List your sprinter van for short-term rentals and trips.",
        "Website": "https://www.turo.com",
    },
    {
        "Name": "Getaround",
        "Category": "Transportation Platforms",
        "Description": "Offer your vehicles for flexible peer-to-peer car sharing.",
        "Website": "https://www.getaround.com",
    },
    {
        "Name": "Shofur",
        "Category": "Transportation Platforms",
        "Description": "Specialized in bus rentals for events and group travel.",
        "Website": "https://www.shofur.com",
    },
    {
        "Name": "BusRates",
        "Category": "Transportation Platforms",
        "Description": "A directory where customers can find and compare bus services.",
        "Website": "https://www.busrates.com",
    },
    {
        "Name": "WeddingWire",
        "Category": "Event & Wedding Platforms",
        "Description": "Reach couples planning weddings who need transportation services.",
        "Website": "https://www.weddingwire.com",
    },
    {
        "Name": "The Knot",
        "Category": "Event & Wedding Platforms",
        "Description": "A popular wedding marketplace to promote transportation options.",
        "Website": "https://www.theknot.com",
    },
    {
        "Name": "Party Bus Rentals",
        "Category": "Transportation Platforms",
        "Description": "Advertise your party bus services directly to event planners.",
        "Website": "https://www.partybus-rentals.com",
    },
    {
        "Name": "Limos.com",
        "Category": "Transportation Platforms",
        "Description": "Specialized platform for limos and high-end transportation services.",
        "Website": "https://www.limos.com",
    },
    {
        "Name": "Busrental.com",
        "Category": "Transportation Platforms",
        "Description": "Market your bus and sprinter van rentals to a wide audience.",
        "Website": "https://www.busrental.com",
    },
    {
        "Name": "Rent My Party Bus",
        "Category": "Transportation Platforms",
        "Description": "Focuses on party bus rentals for special events.",
        "Website": "https://www.rentmypartybus.com",
    },
    {
        "Name": "Bus.com",
        "Category": "Transportation Platforms",
        "Description": "A comprehensive platform for bus services, including event rentals.",
        "Website": "https://www.bus.com",
    },
    {
        "Name": "CharterUP",
        "Category": "Transportation Platforms",
        "Description": "Find clients who need charter buses for corporate and group travel.",
        "Website": "https://www.charterup.com",
    },
    {
        "Name": "Peerspace",
        "Category": "General Marketplaces",
        "Description": "Promote your services to hosts organizing parties and events.",
        "Website": "https://www.peerspace.com",
    },
    {
        "Name": "Snappr Weddings",
        "Category": "Event & Wedding Platforms",
        "Description": "A great option to advertise your services alongside wedding vendors.",
        "Website": "https://www.snappr.com/weddings",
    },
    {
        "Name": "TikTok (Business Account)",
        "Category": "Social Media Platforms",
        "Description": "Reach a younger audience with creative, engaging video content.",
        "Website": "https://www.tiktok.com",
    },
    {
        "Name": "LinkedIn (Business Page)",
        "Category": "Social Media Platforms",
        "Description": "Promote corporate event transportation to professionals.",
        "Website": "https://www.linkedin.com",
    },
    {
        "Name": "Pinterest",
        "Category": "Social Media Platforms",
        "Description": "Share images of your vehicles and event setups to inspire planners.",
        "Website": "https://www.pinterest.com",
    },
    {
        "Name": "Travelocity",
        "Category": "General Marketplaces",
        "Description": "Reach travelers needing group transportation.",
        "Website": "https://www.travelocity.com",
    },
]

# Filters
st.sidebar.header("Filter Listings")
selected_category = st.sidebar.selectbox("Choose a category", ["All"] + categories)

# Filter platforms based on selection
if selected_category != "All":
    filtered_platforms = [p for p in platforms if p["Category"] == selected_category]
else:
    filtered_platforms = platforms

# Search Functionality
search_query = st.sidebar.text_input("Search Listings")
if search_query:
    filtered_platforms = [
        p
        for p in filtered_platforms
        if search_query.lower() in p["Name"].lower()
        or search_query.lower() in p["Description"].lower()
    ]

# Display filtered platforms
st.write(f"### Showing {len(filtered_platforms)} results:")
for platform in filtered_platforms:
    st.write(f"#### {platform['Name']}")
    st.write(f"*Category:* {platform['Category']}")
    st.write(f"*Description:* {platform['Description']}")
    st.markdown(f"[Visit Website]({platform['Website']})")
    st.write("---")

# Footer
st.markdown(
    """
    ---
    ### Tips for Success
    - Create a professional profile with high-quality images of your vehicles.
    - Provide detailed descriptions, pricing, and customer testimonials.
    - Engage with potential clients through social media.
    """
)
