from flask import Flask, render_template

app = Flask(__name__)

# 1. Define your data at the top so both functions can see it
products_data = {
    # --- Management Tools ---
    'cloud-ledger': {
        'name': 'Cloud Ledger',
        'price': '$29',
        'desc': 'Automated bookkeeping designed for high-volume cafes.',
        'img': 'image/element/LABEL.jpg'
    },
    'asset-tracker': {
        'name': 'Asset Tracker',
        'price': '$49',
        'desc': 'Real-time inventory sync with smart low-stock alerts.',
        'img': 'image/element/LABEL.jpg'
    },
    'payroll-pro': {
        'name': 'Payroll Pro',
        'price': '$19',
        'desc': 'Simplified salary distribution and local tax compliance.',
        'img': 'image/element/LABEL.jpg'
    },
    'audit-shield': {
        'name': 'Audit Shield',
        'price': '$99',
        'desc': 'Enterprise-grade reporting for tax-season peace of mind.',
        'img': 'image/element/LABEL.jpg'
    },
    'shift-sync': {
        'name': 'Shift Sync',
        'price': '$15',
        'desc': 'Smart employee scheduling with automated break tracking.',
        'img': 'image/element/LABEL.jpg'
    },

    # --- Cafe Essentials ---
    'bean-minder': {
        'name': 'Bean Minder',
        'price': '$12',
        'desc': 'Track roast dates and freshness levels for every batch.',
        'img': 'image/element/LABEL.jpg'
    },
    'brew-logic': {
        'name': 'Brew Logic',
        'price': '$35',
        'desc': 'Recipe management and consistency tool for baristas.',
        'img': 'image/element/LABEL.jpg'
    },
    'temp-guard': {
        'name': 'Temp Guard',
        'price': '$45',
        'desc': 'IoT integration for fridge and espresso machine monitoring.',
        'img': 'image/element/LABEL.jpg'
    },
    'order-flow': {
        'name': 'Order Flow',
        'price': '$25',
        'desc': 'Streamlined KDS (Kitchen Display System) for busy mornings.',
        'img': 'image/element/LABEL.jpg'
    },
    'loyalty-loop': {
        'name': 'Loyalty Loop',
        'price': '$20',
        'desc': 'Customizable digital stamp cards and customer rewards.',
        'img': 'image/element/LABEL.jpg'
    },

    # --- Customer Experience ---
    'table-tap': {
        'name': 'Table Tap',
        'price': '$30',
        'desc': 'QR-based ordering and payment system for faster service.',
        'img': 'image/element/LABEL.jpg'
    },
    'gift-vault': {
        'name': 'Gift Vault',
        'price': '$10',
        'desc': 'Create and sell digital gift cards directly from your site.',
        'img': 'image/element/LABEL.jpg'
    },
    'event-echo': {
        'name': 'Event Echo',
        'price': '$40',
        'desc': 'Manage cafe events, workshops, and private bookings.',
        'img': 'image/element/LABEL.jpg'
    },
    'feedback-flare': {
        'name': 'Feedback Flare',
        'price': '$5',
        'desc': 'Private customer surveys to capture sentiment instantly.',
        'img': 'image/element/LABEL.jpg'
    },

    # --- Premium Insights ---
    'profit-pilot': {
        'name': 'Profit Pilot',
        'price': '$150',
        'desc': 'AI-driven financial forecasting and wastage analysis.',
        'img': 'image/element/LABEL.jpg'
    },
    'market-mapper': {
        'name': 'Market Mapper',
        'price': '$85',
        'desc': 'Track local competitor pricing and market trends.',
        'img': 'image/element/LABEL.jpg'
    },
    'vendor-view': {
        'name': 'Vendor View',
        'price': '$55',
        'desc': 'Consolidated dashboard for managing multiple suppliers.',
        'img': 'image/element/LABEL.jpg'
    },
    'carbon-count': {
        'name': 'Carbon Count',
        'price': '$15',
        'desc': 'Measure and report on your cafe’s sustainability metrics.',
        'img': 'image/element/LABEL.jpg'
    },
    'queue-crunch': {
        'name': 'Queue Crunch',
        'price': '$65',
        'desc': 'Visual data on wait times and staff efficiency peaks.',
        'img': 'image/element/LABEL.jpg'
    },
    'secure-serve': {
        'name': 'Secure Serve',
        'price': '$120',
        'desc': 'Total POS encryption and digital security suite.',
        'img': 'image/element/LABEL.jpg'
    }
}


@app.route('/')
def home():
    return render_template('homepage.html')

# 2. This route handles the GRID (all products)
@app.route('/product')
def product():
    return render_template('product.html', products=products_data)

# 3. This route handles the DETAIL (one specific product)
@app.route('/product/<product_id>')
def product_detail(product_id):
    # Fetch the specific item using the ID from the URL
    item = products_data.get(product_id)
    if not item:
        return "Product not found", 404
    return render_template('product_detail.html', item=item)
@app.route('/about_us')
def about_us():
    return render_template('about.html')
@app.route('/franchise')
def franchise():
    return render_template('franchise.html')
if __name__ == '__main__':
    app.run(debug=True)