from playwright.sync_api import sync_playwright
import json

def scrape_principal_details(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/administrations')

    button_selector = ".sidebar-nav-li:has-text('Principal')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.grid') 
    name = page.locator('.custom-a p').text_content()
    position = page.locator('.person-position').text_content()
    email = page.locator('.bio-contact-item a').get_attribute('href').replace('mailto:', '')
    image_url = page.locator('.bio-img img').get_attribute('src')
    profile_link = page.locator('.person-name').locator('..').get_attribute('href') 

    principal_details = {
        "Name of Principal": name,
        "Position of Principal": position,
        "Email of Principal": email,
        "Image URL of Principal": image_url,
        "Profile Link of Principal": profile_link,
    }

    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(principal_details, file, ensure_ascii=False, indent=4)

    browser.close()

def scrape_about_section(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/administrations')
    button_selector = ".sidebar-nav-li:has-text('About')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.about')
    about_text = page.locator('.about .about-content .custom-p').text_content()
    about_details = {
        "About Model Engineering College": about_text
    }  
    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {} 
    existing_data.update(about_details)
    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    browser.close()
def scrape_board_of_governors_section(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/administrations')
    button_selector = ".sidebar-nav-li:has-text('Board-of-Governers')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.board')
    description = page.locator('.board .custom-p').text_content().replace("\r", "").replace("\n", "").strip(),
    members = []
    for member in page.locator('.photo-item').all():
        member_details = {
            "Name": member.locator('.person-name').text_content().replace("\r", "").replace("\n", "").strip(),
            "Position": member.locator('.person-position').text_content().replace("\r", "").replace("\n", "").strip(),
            "Description": member.locator('p:nth-child(4)').text_content().replace("\r", "").replace("\n", "").strip(),
            "Image URL": member.locator('img').get_attribute('src').replace("\r", "").replace("\n", "").strip(),
        }
        members.append(member_details)

    board_details = {
        "Description of board of governors": description,
        "Members of board of governors": members
    } 
    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {} 
    existing_data.update(board_details)
    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    browser.close()

def scrape_administrative_staff_section(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/administrations')
    button_selector = ".sidebar-nav-li:has-text('Administrative Staff')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.board')
    staff_members = []
    for member in page.locator('.board .photo-item').all():
        member_details = {
            "Name": member.locator('.person-name').text_content().strip(),
            "Position": member.locator('.person-position').text_content().strip(),
            "Image URL": member.locator('img').get_attribute('src'),
            # Some members have additional description (like "On deputation")
            "Additional Info": member.locator('p:nth-child(4)').text_content().strip() if member.locator('p:nth-child(4)').count() > 0 else ""
        }
        staff_members.append(member_details)

    admin_staff_details = {
        "Administrative_Staff of Model Engineering College": staff_members
    } 
    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {} 
    existing_data.update(admin_staff_details)
    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    browser.close()

def scrape_academic_council_section(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/administrations')
    button_selector = ".sidebar-nav-li:has-text('Academic Council')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.grid')
    description = page.locator('.grid > .custom-p').text_content()
    
    members = []
    for member in page.locator('.grid .photo-item').all():
        member_details = {
            "Name": member.locator('.person-name').text_content().strip(),
            "Position": member.locator('.person-position').text_content().strip(),
            "Description": member.locator('p:nth-child(4)').text_content().strip() if member.locator('p:nth-child(4)').count() > 0 else "",
            "Image URL": member.locator('img').get_attribute('src')
        }
        members.append(member_details)

    functions = []
    for function in page.locator('.function-list ul li').all():
        functions.append(function.text_content().strip())

    academic_council_details = {
        "Description of Academic Council": description,
        "Members of Academic Council": members,
        "Functions of Academic Council": functions
    } 
    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {} 
    existing_data.update(academic_council_details)
    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    browser.close()

def scrape_pta_section(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/administrations')
    button_selector = ".sidebar-nav-li:has-text('PTA')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.page-content')
    description = page.locator('.page-content .custom-p').text_content()
    members = []
    for member in page.locator('.list-image-container .photo-item').all():
        member_details = {
            "Name": member.locator('.person-name').text_content().strip(),
            "Position": member.locator('.person-position').text_content().strip(),
            "Image URL": member.locator('img').get_attribute('src')
        }
        members.append(member_details)

    pta_details = {
        "Description of PTA": description,
        "Members of PTA": members
    } 
    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {} 
    existing_data.update(pta_details)
    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    browser.close()

def scrape_senate_section(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/administrations')
    button_selector = ".sidebar-nav-li:has-text('Senate')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.Senate')
    description = page.locator('.Senate > .custom-p').text_content()
    members = []
    for member in page.locator('.Senate .photo-item').all():
        member_details = {
            "Name": member.locator('.person-name').text_content().strip(),
            "Position": member.locator('.person-position').text_content().strip(),
            "Additional Info": member.locator('p:nth-child(4)').text_content().strip() if member.locator('p:nth-child(4)').count() > 0 else "",
            "Image URL": member.locator('img').get_attribute('src')
        }
        members.append(member_details)

    senate_details = {
        "Description of Senate": description,
        "Members of Senate": members
    } 
    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {} 
    existing_data.update(senate_details)
    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    browser.close()



def scrape_admission_details_section(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/admissions2024')
    page.wait_for_selector('.admission')
    admission_procedure = page.locator('.admission p').text_content()

    ug_programmes = []
    for card in page.locator('.admissioncardholder .admissionscard').all():
        programme = {
            "Programme": card.locator('h3').text_content().strip(),
            "Course": card.locator('.course-admission2k23').text_content().strip(),
            "Seats": card.locator('.seats-admission2k23').text_content().strip(),
            "Is New": True if card.locator('#newbadge').count() > 0 else False
        }
        ug_programmes.append(programme)
    fee_structure = []
    for row in page.locator('.fee-table tbody tr').all():
        fee = {
            "Category": row.locator('td:nth-child(1)').text_content().strip(),
            "Amount": row.locator('td:nth-child(2)').text_content().strip()
        }
        fee_structure.append(fee)
    seat_matrix = {
        "Merit Regulated": "50%",
        "Merit Full Fees": "45%",
        "NRI": "5%"
    }

    pg_programmes = []
    for card in page.locator('.admissioncardholder:nth-child(2) .admissionscard').all():
        programme = {
            "Programme": card.locator('h3').text_content().strip(),
            "Course": card.locator('.course-admission2k23').text_content().strip(),
            "Seats": card.locator('.seats-admission2k23').text_content().strip()
        }
        pg_programmes.append(programme)

    admission_details = {
        "Admission_Procedure": admission_procedure,
        "UG_Programmes": ug_programmes,
        "Fee_Structure": fee_structure,
        "Seat_Matrix": seat_matrix,
        "PG_Programmes": pg_programmes
    } 
    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {} 
    existing_data.update(admission_details)
    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    browser.close()

def scrape_facilities(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/facilities')
    
    facilities = []

    for facility in page.locator('.facilities-page-items .gen-facility-item').all():
        facility_details = {
            "Name": facility.locator('.custom-h3').text_content().strip().replace('\xa0', ''),
            "Description": facility.locator('.custom-p').text_content().strip(),
            # "Icon URL": facility.locator('.facility-icon').get_attribute('src'),
            # "Link": facility.locator('a').get_attribute('href') if facility.locator('a').count() > 0 else None
        }
        facilities.append(facility_details)
    library_details = {
        "Name": "Library",
        "Description": page.locator('.page-content > div:last-child > div > .custom-p').text_content().strip(),
        # "Icon URL": page.locator('img[alt="library"]').get_attribute('src'),
        # "Link": page.locator('.custom-a').get_attribute('href')
    }
    facilities.append(library_details)

    facilities_details = {
        "Facilities in Model Engineering College": facilities
    }

    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(facilities_details)

    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

    browser.close()

def scrape_about_statutory_committee(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/committees')
    button_selector = ".sidebar-nav-li:has-text('About')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.about')
    about_text = page.locator('.about .custom-p').text_content()
    
    about_details = {
        "About_Statutory_Committees": about_text
    }

    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(about_details)

    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

    browser.close()

def scrape_iqac_section(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/committees')
    button_selector = ".sidebar-nav-li:has-text('Internal Quality Assurance Cell')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.grid')
    description = page.locator('.grid > .custom-p').text_content()
    
    functions = []
    for item in page.locator('.grid ul li').all():
        functions.append(item.text_content().strip())
    
    meeting_minutes = []
    for link in page.locator('.grid > a').all():
        meeting_minutes.append({
            "Title": link.text_content().strip(),
            "URL": link.get_attribute('href')
        })
    
    members = []
    for member in page.locator('.list-image-container .photo-item').all():
        member_details = {
            "Name": member.locator('.person-name').text_content().strip(),
            "Position": member.locator('.person-position').text_content().strip(),
            "Additional Info": member.locator('p:nth-child(4)').text_content().strip() if member.locator('p:nth-child(4)').count() > 0 else "",
            "Image URL": member.locator('img').get_attribute('src')
        }
        members.append(member_details)

    iqac_details = {
        "Description of Internal Quality Assurance Cell": description,
        "Functions of Internal Quality Assurance Cell": functions,
        "Meeting Minutes of Internal Quality Assurance Cell": meeting_minutes,
        "Members of Internal Quality Assurance Cell": members
    }

    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(iqac_details)

    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

    browser.close()

def scrape_grievance_cell(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/committees')
    button_selector = ".sidebar-nav-li:has-text('Grievance Cell')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.about')
    description = page.locator('.about > .custom-p').text_content()
    
    members = []
    for member in page.locator('.list-image-container .photo-item').all():
        member_details = {
            "Name": member.locator('.person-name').text_content().strip(),
            "Position": member.locator('.person-position').text_content().strip(),
            "Image URL": member.locator('img').get_attribute('src')
        }
        members.append(member_details)

    grievance_cell_details = {
        "Description of grievance cell": description,
        "Members of grievance cell": members
    }

    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(grievance_cell_details)

    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

    browser.close()


def scrape_anti_ragging_committee(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/committees')
    button_selector = ".sidebar-nav-li:has-text('Anti-ragging Committee')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.about')
    description = page.locator('.about > .custom-p').first.text_content()
    
    # Get references
    references = []
    for item in page.locator('.about ol li').all():
        references.append(item.text_content().strip())
    
    # Get committee members
    members = []
    members.append({
        "Position": "Chairman",
        "Name": "Principal"
    })
    members.append({
        "Position": "Member Secretary",
        "Name": "Dr. Sreenivas P, Associate Prof. in Mechanical (Chairman – Anti ragging squad.)"
    })

    anti_ragging_committee_details = {
        "Description of anti_ragging_committee_details": description,
        "References of anti_ragging_committee_details": references,
        "Members of anti_ragging_committee_details": members
    }

    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(anti_ragging_committee_details)

    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

    browser.close()


def scrape_anti_ragging_squad(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/committees')
    button_selector = ".sidebar-nav-li:has-text('Anti-Ragging Squad')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.about')
    description = page.locator('.about > .custom-p').first.text_content()
    
    references = []
    for item in page.locator('.about ol li').all():
        references.append(item.text_content().strip())
    
    members = []
    for member in page.locator('.list-image-container .photo-item').all():
        member_details = {
            "Name": member.locator('.person-name').text_content().strip(),
            "Position": member.locator('.person-position').text_content().strip(),
            "Additional Info": member.locator('p:nth-child(4)').text_content().strip() if member.locator('p:nth-child(4)').count() > 0 else "",
            "Image URL": member.locator('img').get_attribute('src')
        }
        members.append(member_details)

    anti_ragging_squad_details = {
        "Description of anti ragging squad": description,
        "References of anti ragging squad": references,
        "Members of anti ragging squad": members
    }

    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(anti_ragging_squad_details)

    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

    browser.close()


def scrape_anti_sexual_harassment_cell(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/committees')
    button_selector = ".sidebar-nav-li:has-text('Anti-sexual Harassment & Internal Compliance Cell')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.about')
    descriptions = page.locator('.about > p.custom-p').all()
    main_description = "\n".join([desc.text_content().strip() for desc in descriptions[:2]])
    
    # Get objectives
    objectives = []
    for item in page.locator('.about > ul').first.locator('li').all():
        objectives.append(item.text_content().strip())
    
    # Get definition of sexual harassment
    harassment_definition = page.locator('.about > p.custom-p').nth(2).text_content()
    harassment_types = []
    for item in page.locator('.about > ul').nth(1).locator('li').all():
        harassment_types.append(item.text_content().strip())
    
    # Get committee members
    members = []
    for member in page.locator('.list-image-container .photo-item').all():
        member_details = {
            "Name": member.locator('.person-name').text_content().strip(),
            "Position": member.locator('.person-position').text_content().strip(),
            "Contact": member.locator('p:nth-child(4)').text_content().strip() if member.locator('p:nth-child(4)').count() > 0 else "",
            "Image URL": member.locator('img').get_attribute('src')
        }
        members.append(member_details)
    
    # Get complaint handling info
    complaint_info = page.locator('.about > p.custom-p').nth(-2).text_content()
    false_reporting_info = page.locator('.about > p.custom-p').nth(-1).text_content()
    
    # Get links
    handbook_link = page.locator('a[href*="Anti-Sexual-Harrassment-Handbook.pdf"]').get_attribute('href')
    complaint_form_link = page.locator('a[href*="forms.gle"]').get_attribute('href')

    cell_details = {
        "Description of Anti-sexual Harassment & Internal Compliance Cell": main_description,
        "Objectives of Anti-sexual Harassment & Internal Compliance Cell": objectives,
        "Sexual_Harassment_Definition": harassment_definition,
        "Types_of_Sexual_Harassment": harassment_types,
        "Members of Anti-sexual Harassment & Internal Compliance Cell": members,
        "Complaint_Handling of Anti-sexual Harassment & Internal Compliance Cell": complaint_info,
        "False_Reporting": false_reporting_info,
        "Handbook_Link": handbook_link,
        "Complaint_Form_Link of Anti-sexual Harassment & Internal Compliance Cell": complaint_form_link
    }

    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(cell_details)

    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

    browser.close()

def scrape_safety_manual(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/committees')
    button_selector = ".sidebar-nav-li:has-text('Safety Manual')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    page.wait_for_selector('.page-content .about', timeout=5000)
    description = page.locator('.page-content .about p.custom-p').first.text_content().strip()   
    manual_link = page.locator('a[href*="safety_manual.pdf"]').get_attribute('href')
    safety_manual_details = {
        "Description of safety manual": description,
        "Safety Manual Download Link": manual_link
    }

    try:
        with open("MEC.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(safety_manual_details)

    with open("MEC.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

    browser.close()

def comp_sci_section(playwright,section_name, output_file="MEC.json"):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/departments/cse')

    button_selector = f".sidebar-nav-li:has-text('{section_name}')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    
    section_data = {}
    if section_name == "About":
        page.wait_for_selector('.about')
        section_data = {
            "Description": page.locator('.about > .custom-p').text_content().strip()
        }
    elif section_name == "Vision & Mission":
        
        page.wait_for_selector('.vision-mission')

        vision = page.locator('.vision .custom-p').text_content().strip()

        mission_items = []
        for item in page.locator('.mission-item').all():

            paragraphs = item.locator('.custom-p').all()
            if len(paragraphs) >= 2: 
                mission_number = paragraphs[0].text_content().strip()  
                mission_text = paragraphs[1].text_content().strip()   
                mission_items.append({
                    # "Number": mission_number,
                    f"Description of mission {mission_number}": mission_text
                })
        
        peos = []
        peo_items = page.locator('h2:text("Program Educational Objectives") ~ .ed-obj .ed-obj-item').all()
        for peo in peo_items:
            if peo.locator('.custom-h3').count() > 0 and peo.locator('.custom-p').count() > 0:
                peos.append({
                    # "Title": peo.locator('.custom-h3').text_content().strip(),
                    f"Description of {peo.locator('.custom-h3').text_content().strip()}": peo.locator('.custom-p').text_content().strip()
                })

        psos = []
        pso_items = page.locator('h2:text("Program Specific Outcomes") ~ .ed-obj .ed-obj-item').all()
        for pso in pso_items:
            if pso.locator('.custom-h3').count() > 0 and peo.locator('.custom-p').count() > 0:
                psos.append({
                    # "Title": pso.locator('.custom-h3').text_content().strip(),
                    f"Description of {pso.locator('.custom-h3').text_content().strip()}": pso.locator('.custom-p').text_content().strip()
                })
        pos = []
        po_items = page.locator('h2:text("Program Outcomes") ~ .ed-obj .ed-obj-item').all()
        for po in po_items:
            if po.locator('.custom-h3').count() > 0 and po.locator('.custom-p').count() > 0:
                pos.append({
                    # "Title": po.locator('.custom-h3').text_content().strip(),
                    f"Description of {po.locator('.custom-h3').text_content().strip()}": po.locator('.custom-p').text_content().strip()
                })
                
        section_data = {
            "Vision": vision,
            "Mission": mission_items,
            "Program_Educational_Objectives": peos,
            "Program_Specific_Outcomes": psos,
            "Program_Outcomes": pos
        }

    elif section_name == "Courses Offered":
        page.wait_for_selector('.courses-offered')
        courses = []
        
        course_items = page.locator('.course-item').all()
        for item in course_items:
            course_details = {
                "Degree": item.locator('.custom-h2').text_content().strip(),
                "Program": item.locator('.custom-h2').text_content().strip()+" "+item.locator('.custom-h3.red').first.text_content().strip()
            }

            if item.locator('.custom-h3.red').count() > 1:
                course_details["Specialization"] = item.locator('.custom-h3.red').nth(1).text_content().strip(),
                course_details["Program"] += f" with specialization in {item.locator('.custom-h3.red').nth(1).text_content().strip()}"
            courses.append(course_details)
            
        section_data = {
            "Courses offered in computer science": courses
        }
    elif section_name == "HOD":
        page.wait_for_selector('.grid')
        page.wait_for_selector('.photo-item .person-name', state='visible')
        page.wait_for_selector('.photo-item .person-position', state='visible')

        section_data = {
            "Name of HOD": page.locator('.photo-item .person-name').text_content().strip(),
            "Position of HOD": page.locator('.photo-item .person-position').text_content().strip(),
            "Email of HOD": page.locator('.bio-contact-item a').get_attribute('href').replace('mailto:', ''),
            "Image URL of HOD": page.locator('.photo-item img').get_attribute('src'),
        }
    elif section_name == "Faculty":
        page.wait_for_selector('.grid')
        faculty_members = []
        page.wait_for_selector('.photo-item',state = 'visible')
        page.wait_for_selector('.photo-item .person-name', state='visible')
        page.wait_for_selector('.photo-item .person-position', state='visible')
        for member in page.locator('.photo-item').all():
            faculty_details = {
                "Name": member.locator('.person-name').text_content().strip(),
                "Position": member.locator('.person-position').text_content().strip(),
                "Image URL": member.locator('img').get_attribute('src')
            }
        
            # profile_link = member.locator('.custom-a').get_attribute('href')
            # if profile_link:
            #     faculty_details["Profile Link"] = profile_link
                
            faculty_members.append(faculty_details)
            
        section_data = {
            "Faculty_Members of computer science": faculty_members
        }
    elif section_name == "Facilities":
        page.wait_for_selector('.page-content')
        
        # Get main description
        main_description = page.locator('.page-content > div > .custom-p').first.text_content().strip()
        
        # Get all facilities
        facilities = []
        for facility in page.locator('.facility-items > div').all():
            facility_details = {
                "Name": facility.locator('.custom-h3').text_content().strip(),
                f"Description of {facility.locator('.custom-h3').text_content().strip()}": facility.locator('.custom-p').text_content().strip()
            }
            facilities.append(facility_details)
            
        section_data = {
            "Main_Description of facilities offered in computer science": main_description,
            "Facilities offered in computer science": facilities
        }
    elif section_name == "Resources":
        page.wait_for_selector('.page-content')
        main_description = page.locator('.page-content > div > .custom-p').first.text_content().strip()
        
        resources = []
        for resource in page.locator('.res > div').all():
            resource_details = {
                # "Name": resource.locator('.custom-h3').text_content().strip(),
                f"Description of {resource.locator('.custom-h3').text_content().strip()}": resource.locator('.custom-p').text_content().strip(),
                "Links": [
                    {
                        # "Title": link.text_content().strip(),
                        # "URL ": link.get_attribute('href')
                        f"URL of {link.text_content().strip()}": link.get_attribute('href')
                    }
                    for link in resource.locator('.custom-a').all()
                ]
            }
            resources.append(resource_details)
            
        section_data = {
            "Main_Description": main_description,
            "Resources available in computer science": resources
        }  

    elif section_name == "Associations":
        page.wait_for_selector('.asc')
        
        section_data = {
            "Name": page.locator('.asc .custom-h3').text_content().strip(),
            "Description of association in computer science": page.locator('.asc .custom-p').text_content().strip()
        }

    elif section_name == "Achievements":
        page.wait_for_selector('.page-content')
        
        main_description = page.locator('.page-content > div > div > .custom-p').text_content().strip()
        page.wait_for_selector('.std-achievements ul > li')
        achievements = []
        c=0
        for item in page.locator('.std-achievements ul > li').all():
            achievement_text = item.inner_text().strip()
            if item.locator('b').count() > 0:
                title = item.locator('b').text_content().strip()
                if item.locator('ol').count() > 0:
                    sub_achievements = [
                        li.text_content().strip() 
                        for li in item.locator('ol > li').all()
                    ]
                    achievements.append({
                        "Title": title,
                        f"Sub_Achievements like {title}": sub_achievements
                    })
                else:
                    content = achievement_text.replace(title, '').strip()
                    achievements.append({
                        "Title": title,
                        f"{title} Description": content
                    })
            else:
                c+=1
                achievements.append({                   
                    f"Description of achievement {c}": achievement_text
                })
        section_data = {
            "Main_Description": main_description,
            "Achievements of computer science department": achievements
        } 
    elif section_name == "Recent Projects":
        page.wait_for_selector('.page-content')
        main_description = page.locator('.page-content > div > div > .custom-p').first.text_content().strip()
        page.wait_for_selector('.project-item')
        projects = []
        for project in page.locator('.project-item').all():
            project_details = {
                # "Title": project.locator('.custom-h3').text_content().strip(),
                f"Description of {project.locator('.custom-h3').text_content().strip()}": project.locator('.custom-p').text_content().strip()
            }
            links = project.locator('a').all()
            if links:
                project_details["Links"] = [
                    {
                        # "Text": link.text_content().strip(),
                        f"URL of {link.text_content().strip()}": link.get_attribute('href')
                    }
                    for link in links
                ]
            
            projects.append(project_details)
            
        section_data = {
            "Main_Description of projects in computer science": main_description,
            "Projects of computer science department": projects
        }

    try:
        with open(output_file, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    
    # Update and write the data
    existing_data.update(section_data)
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    
    browser.close()

def electronics_and_communication_section(playwright,section_name, output_file="MEC.json"):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/departments/ece')

    button_selector = f".sidebar-nav-li:has-text('{section_name}')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    
    section_data = {}
    if section_name == "About":
        page.wait_for_selector('.about')
        section_data = {
            "Description": page.locator('.about > .custom-p').text_content().strip()
        }
    elif section_name == "Vision & Mission":
        
        page.wait_for_selector('.vision-mission')

        vision = page.locator('.vision .custom-p').text_content().strip()

        mission_items = []
        for item in page.locator('.mission-item').all():

            paragraphs = item.locator('.custom-p').all()
            if len(paragraphs) >= 2: 
                mission_number = paragraphs[0].text_content().strip()  
                mission_text = paragraphs[1].text_content().strip()   
                mission_items.append({
                    # "Number": mission_number,
                    f"Description of mission {mission_number}": mission_text
                })
        
        peos = []
        peo_items = page.locator('h2:text("Program Educational Objectives") ~ .ed-obj .ed-obj-item').all()
        for peo in peo_items:
            if peo.locator('.custom-h3').count() > 0 and peo.locator('.custom-p').count() > 0:
                peos.append({
                    # "Title": peo.locator('.custom-h3').text_content().strip(),
                    f"Description of {peo.locator('.custom-h3').text_content().strip()}": peo.locator('.custom-p').text_content().strip()
                })

        psos = []
        pso_items = page.locator('h2:text("Program Specific Outcomes") ~ .ed-obj .ed-obj-item').all()
        for pso in pso_items:
            if pso.locator('.custom-h3').count() > 0 and peo.locator('.custom-p').count() > 0:
                psos.append({
                    # "Title": pso.locator('.custom-h3').text_content().strip(),
                    f"Description of {pso.locator('.custom-h3').text_content().strip()}": pso.locator('.custom-p').text_content().strip()
                })
        pos = []
        po_items = page.locator('h2:text("Program Outcomes") ~ .ed-obj .ed-obj-item').all()
        for po in po_items:
            if po.locator('.custom-h3').count() > 0 and po.locator('.custom-p').count() > 0:
                pos.append({
                    # "Title": po.locator('.custom-h3').text_content().strip(),
                    f"Description of {po.locator('.custom-h3').text_content().strip()}": po.locator('.custom-p').text_content().strip()
                })
                
        section_data = {
            "Vision": vision,
            "Mission": mission_items,
            "Program_Educational_Objectives": peos,
            "Program_Specific_Outcomes": psos,
            "Program_Outcomes": pos
        }

    elif section_name == "Courses Offered":
        page.wait_for_selector('.courses-offered')
        courses = []
        
        course_items = page.locator('.course-item').all()
        for item in course_items:
            course_details = {
                "Degree": item.locator('.custom-h2').text_content().strip(),
                "Program": item.locator('.custom-h2').text_content().strip()+" "+item.locator('.custom-h3.red').first.text_content().strip()
            }

            if item.locator('.custom-h3.red').count() > 1:
                course_details["Specialization"] = item.locator('.custom-h3.red').nth(1).text_content().strip(),
                course_details["Program"] += f" with specialization in {item.locator('.custom-h3.red').nth(1).text_content().strip()}"
            courses.append(course_details)
            
        section_data = {
            "Courses offered in electronics and communication": courses
        }
    elif section_name == "HOD":
        page.wait_for_selector('.grid')
        page.wait_for_selector('.photo-item .person-name', state='visible')
        page.wait_for_selector('.photo-item .person-position', state='visible')

        section_data = {
            "Name of HOD": page.locator('.photo-item .person-name').text_content().strip(),
            "Position of HOD": page.locator('.photo-item .person-position').text_content().strip(),
            "Email of HOD":page.locator('.bio-contact-item a').get_attribute('href').replace('mailto:', '') if page.locator('.bio-contact-item a').count() > 0 else None,
            "Image URL of HOD": page.locator('.photo-item img').get_attribute('src'),
        }
    elif section_name == "Faculty":
        page.wait_for_selector('.grid')
        faculty_members = []
        page.wait_for_selector('.photo-item',state = 'visible')
        page.wait_for_selector('.photo-item .person-name', state='visible')
        page.wait_for_selector('.photo-item .person-position', state='visible')
        for member in page.locator('.photo-item').all():
            faculty_details = {
                "Name": member.locator('.person-name').text_content().strip(),
                "Position": member.locator('.person-position').text_content().strip(),
                "Image URL": member.locator('img').get_attribute('src')
            }
        
            # profile_link = member.locator('.custom-a').get_attribute('href')
            # if profile_link:
            #     faculty_details["Profile Link"] = profile_link
                
            faculty_members.append(faculty_details)
            
        section_data = {
            "Faculty_Members of electronics and communication": faculty_members
        }
    elif section_name == "Facilities":
        page.wait_for_selector('.page-content')
        
        # Get main description
        main_description = page.locator('.page-content > div > .custom-p').first.text_content().strip()
        
        # Get all facilities
        facilities = []
        for facility in page.locator('.facility-items > div').all():
            facility_details = {
                "Name": facility.locator('.custom-h3').text_content().strip(),
                f"Description of {facility.locator('.custom-h3').text_content().strip()}": facility.locator('.custom-p').text_content().strip()
            }
            facilities.append(facility_details)
            
        section_data = {
            "Main_Description of facilities offered in electronics and communication": main_description,
            "Facilities offered in electronics and communication": facilities
        }
    elif section_name == "Resources":
        page.wait_for_selector('.page-content')
        main_description = page.locator('.page-content > div > .custom-p').first.text_content().strip()
        
        resources = []
        for resource in page.locator('.res > div').all():
            resource_details = {
                # "Name": resource.locator('.custom-h3').text_content().strip(),
                f"Description of {resource.locator('.custom-h3').text_content().strip()}": resource.locator('.custom-p').text_content().strip(),
                "Links": [
                    {
                        # "Title": link.text_content().strip(),
                        # "URL ": link.get_attribute('href')
                        f"URL of {link.text_content().strip()}": link.get_attribute('href')
                    }
                    for link in resource.locator('.custom-a').all()
                ]
            }
            resources.append(resource_details)
            
        section_data = {
            "Main_Description": main_description,
            "Resources available in electronics and communication": resources
        }  

    elif section_name == "Associations":
        page.wait_for_selector('.asc')
        
        section_data = {
            "Name": page.locator('.asc .custom-h3').text_content().strip(),
            "Description of association in electronics and communication": page.locator('.asc .custom-p').text_content().strip()
        }

    elif section_name == "Achievements":
        page.wait_for_selector('.page-content')
        
        main_description = page.locator('.page-content > div > div > .custom-p').text_content().strip()
        page.wait_for_selector('.std-achievements ul > li')
        achievements = []
        c=0
        for item in page.locator('.std-achievements ul > li').all():
            achievement_text = item.inner_text().strip()
            if item.locator('b').count() > 0:
                title = item.locator('b').text_content().strip()
                if item.locator('ol').count() > 0:
                    sub_achievements = [
                        li.text_content().strip() 
                        for li in item.locator('ol > li').all()
                    ]
                    achievements.append({
                        "Title": title,
                        f"Sub_Achievements like {title}": sub_achievements
                    })
                else:
                    content = achievement_text.replace(title, '').strip()
                    achievements.append({
                        "Title": title,
                        f"{title} Description": content
                    })
            else:
                c+=1
                achievements.append({                   
                    f"Description of achievement {c}": achievement_text
                })
        section_data = {
            "Main_Description": main_description,
            "Achievements of electronics and communication department": achievements
        } 
    elif section_name == "Recent Projects":
        page.wait_for_selector('.page-content')
        main_description = page.locator('.page-content > div > div > .custom-p').first.text_content().strip()
        page.wait_for_selector('.project-item')
        projects = []
        for project in page.locator('.project-item').all():
            project_details = {
                # "Title": project.locator('.custom-h3').text_content().strip(),
                f"Description of {project.locator('.custom-h3').text_content().strip()}": project.locator('.custom-p').text_content().strip()
            }
            links = project.locator('a').all()
            if links:
                project_details["Links"] = [
                    {
                        # "Text": link.text_content().strip(),
                        f"URL of {link.text_content().strip()}": link.get_attribute('href')
                    }
                    for link in links
                ]
            
            projects.append(project_details)
            
        section_data = {
            "Main_Description of projects in electronics and communication": main_description,
            "Projects of electronics and communication department": projects
        }

    try:
        with open(output_file, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    
    # Update and write the data
    existing_data.update(section_data)
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    
    browser.close()

def electrical_and_electronics_section(playwright,section_name, output_file="MEC.json"):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/departments/eee')

    button_selector = f".sidebar-nav-li:has-text('{section_name}')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    
    section_data = {}
    if section_name == "About":
        page.wait_for_selector('.about')
        section_data = {
            "Description": page.locator('.about > .custom-p').text_content().strip()
        }
    elif section_name == "Vision & Mission":
        
        page.wait_for_selector('.vision-mission')

        vision = page.locator('.vision .custom-p').text_content().strip()

        mission_items = []
        for item in page.locator('.mission-item').all():

            paragraphs = item.locator('.custom-p').all()
            if len(paragraphs) >= 2: 
                mission_number = paragraphs[0].text_content().strip()  
                mission_text = paragraphs[1].text_content().strip()   
                mission_items.append({
                    # "Number": mission_number,
                    f"Description of mission {mission_number}": mission_text
                })
        
        peos = []
        peo_items = page.locator('h2:text("Program Educational Objectives") ~ .ed-obj .ed-obj-item').all()
        for peo in peo_items:
            if peo.locator('.custom-h3').count() > 0 and peo.locator('.custom-p').count() > 0:
                peos.append({
                    # "Title": peo.locator('.custom-h3').text_content().strip(),
                    f"Description of {peo.locator('.custom-h3').text_content().strip()}": peo.locator('.custom-p').text_content().strip()
                })

        psos = []
        pso_items = page.locator('h2:text("Program Specific Outcomes") ~ .ed-obj .ed-obj-item').all()
        for pso in pso_items:
            if pso.locator('.custom-h3').count() > 0 and peo.locator('.custom-p').count() > 0:
                psos.append({
                    # "Title": pso.locator('.custom-h3').text_content().strip(),
                    f"Description of {pso.locator('.custom-h3').text_content().strip()}": pso.locator('.custom-p').text_content().strip()
                })
        pos = []
        po_items = page.locator('h2:text("Program Outcomes") ~ .ed-obj .ed-obj-item').all()
        for po in po_items:
            if po.locator('.custom-h3').count() > 0 and po.locator('.custom-p').count() > 0:
                pos.append({
                    # "Title": po.locator('.custom-h3').text_content().strip(),
                    f"Description of {po.locator('.custom-h3').text_content().strip()}": po.locator('.custom-p').text_content().strip()
                })
                
        section_data = {
            "Vision": vision,
            "Mission": mission_items,
            "Program_Educational_Objectives": peos,
            "Program_Specific_Outcomes": psos,
            "Program_Outcomes": pos
        }

    elif section_name == "Courses Offered":
        page.wait_for_selector('.courses-offered')
        courses = []
        
        course_items = page.locator('.course-item').all()
        for item in course_items:
            course_details = {
                "Degree": item.locator('.custom-h2').text_content().strip(),
                "Program": item.locator('.custom-h2').text_content().strip()+" "+item.locator('.custom-h3.red').first.text_content().strip()
            }

            if item.locator('.custom-h3.red').count() > 1:
                course_details["Specialization"] = item.locator('.custom-h3.red').nth(1).text_content().strip(),
                course_details["Program"] += f" with specialization in {item.locator('.custom-h3.red').nth(1).text_content().strip()}"
            courses.append(course_details)
            
        section_data = {
            "Courses offered in electrical and electronics": courses
        }
    elif section_name == "HOD":
        page.wait_for_selector('.grid')
        page.wait_for_selector('.photo-item .person-name', state='visible')
        page.wait_for_selector('.photo-item .person-position', state='visible')

        section_data = {
            "Name of HOD": page.locator('.photo-item .person-name').text_content().strip(),
            "Position of HOD": page.locator('.photo-item .person-position').text_content().strip(),
            "Email of HOD":page.locator('.bio-contact-item a').get_attribute('href').replace('mailto:', '') if page.locator('.bio-contact-item a').count() > 0 else None,
            "Image URL of HOD": page.locator('.photo-item img').get_attribute('src'),
        }
    elif section_name == "Faculty":
        page.wait_for_selector('.grid')
        faculty_members = []
        page.wait_for_selector('.photo-item',state = 'visible')
        page.wait_for_selector('.photo-item .person-name', state='visible')
        page.wait_for_selector('.photo-item .person-position', state='visible')
        for member in page.locator('.photo-item').all():
            faculty_details = {
                "Name": member.locator('.person-name').text_content().strip(),
                "Position": member.locator('.person-position').text_content().strip(),
                "Image URL": member.locator('img').get_attribute('src')
            }
        
            # profile_link = member.locator('.custom-a').get_attribute('href')
            # if profile_link:
            #     faculty_details["Profile Link"] = profile_link
                
            faculty_members.append(faculty_details)
            
        section_data = {
            "Faculty_Members of electrical and electronics": faculty_members
        }
    elif section_name == "Facilities":
        page.wait_for_selector('.page-content')
        
        # Get main description
        main_description = page.locator('.page-content > div > .custom-p').first.text_content().strip()
        
        # Get all facilities
        facilities = []
        for facility in page.locator('.facility-items > div').all():
            facility_details = {
                "Name": facility.locator('.custom-h3').text_content().strip(),
                f"Description of {facility.locator('.custom-h3').text_content().strip()}": facility.locator('.custom-p').text_content().strip()
            }
            facilities.append(facility_details)
            
        section_data = {
            "Main_Description of facilities offered in electrical and electronics": main_description,
            "Facilities offered in electrical and electronics": facilities
        }
    elif section_name == "Resources":
        page.wait_for_selector('.page-content')
        main_description = page.locator('.page-content > div > .custom-p').first.text_content().strip()
        
        resources = []
        for resource in page.locator('.res > div').all():
            resource_details = {
                # "Name": resource.locator('.custom-h3').text_content().strip(),
                f"Description of {resource.locator('.custom-h3').text_content().strip()}": resource.locator('.custom-p').text_content().strip(),
                "Links": [
                    {
                        # "Title": link.text_content().strip(),
                        # "URL ": link.get_attribute('href')
                        f"URL of {link.text_content().strip()}": link.get_attribute('href')
                    }
                    for link in resource.locator('.custom-a').all()
                ]
            }
            resources.append(resource_details)
            
        section_data = {
            "Main_Description": main_description,
            "Resources available in electrical and electronics": resources
        }  

    elif section_name == "Associations":
        page.wait_for_selector('.asc')
        
        section_data = {
            "Name": page.locator('.asc .custom-h3').text_content().strip(),
            "Description of association in electrical and electronics": page.locator('.asc .custom-p').text_content().strip()
        }

    elif section_name == "Achievements":
        page.wait_for_selector('.page-content')
        
        main_description = page.locator('.page-content > div > div > .custom-p').text_content().strip()
        page.wait_for_selector('.std-achievements ul > li')
        achievements = []
        c=0
        for item in page.locator('.std-achievements ul > li').all():
            achievement_text = item.inner_text().strip()
            if item.locator('b').count() > 0:
                title = item.locator('b').text_content().strip()
                if item.locator('ol').count() > 0:
                    sub_achievements = [
                        li.text_content().strip() 
                        for li in item.locator('ol > li').all()
                    ]
                    achievements.append({
                        "Title": title,
                        f"Sub_Achievements like {title}": sub_achievements
                    })
                else:
                    content = achievement_text.replace(title, '').strip()
                    achievements.append({
                        "Title": title,
                        f"{title} Description": content
                    })
            else:
                c+=1
                achievements.append({                   
                    f"Description of achievement {c}": achievement_text
                })
        section_data = {
            "Main_Description": main_description,
            "Achievements of electrical and electronics department": achievements
        } 
    elif section_name == "Recent Projects":
        page.wait_for_selector('.page-content')
        main_description = page.locator('.page-content > div > div > .custom-p').first.text_content().strip()
        page.wait_for_selector('.project-item')
        projects = []
        for project in page.locator('.project-item').all():
            project_details = {
                # "Title": project.locator('.custom-h3').text_content().strip(),
                f"Description of {project.locator('.custom-h3').text_content().strip()}": project.locator('.custom-p').text_content().strip()
            }
            links = project.locator('a').all()
            if links:
                project_details["Links"] = [
                    {
                        # "Text": link.text_content().strip(),
                        f"URL of {link.text_content().strip()}": link.get_attribute('href')
                    }
                    for link in links
                ]
            
            projects.append(project_details)
            
        section_data = {
            "Main_Description of projects in electrical and electronics": main_description,
            "Projects of electrical and electronics department": projects
        }

    try:
        with open(output_file, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    
    # Update and write the data
    existing_data.update(section_data)
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    
    browser.close()


def electronics_and_biomedical_section(playwright,section_name, output_file="MEC.json"):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/departments/ebe')

    button_selector = f".sidebar-nav-li:has-text('{section_name}')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    
    section_data = {}
    if section_name == "About":
        page.wait_for_selector('.about')
        section_data = {
            "Description": page.locator('.about > .custom-p').text_content().strip()
        }
    elif section_name == "Vision & Mission":
        
        page.wait_for_selector('.vision-mission')

        vision = page.locator('.vision .custom-p').text_content().strip()

        mission_items = []
        for item in page.locator('.mission-item').all():

            paragraphs = item.locator('.custom-p').all()
            if len(paragraphs) >= 2: 
                mission_number = paragraphs[0].text_content().strip()  
                mission_text = paragraphs[1].text_content().strip()   
                mission_items.append({
                    # "Number": mission_number,
                    f"Description of mission {mission_number}": mission_text
                })
        
        peos = []
        peo_items = page.locator('h2:text("Program Educational Objectives") ~ .ed-obj .ed-obj-item').all()
        for peo in peo_items:
            if peo.locator('.custom-h3').count() > 0 and peo.locator('.custom-p').count() > 0:
                peos.append({
                    # "Title": peo.locator('.custom-h3').text_content().strip(),
                    f"Description of {peo.locator('.custom-h3').text_content().strip()}": peo.locator('.custom-p').text_content().strip()
                })

        psos = []
        pso_items = page.locator('h2:text("Program Specific Outcomes") ~ .ed-obj .ed-obj-item').all()
        for pso in pso_items:
            if pso.locator('.custom-h3').count() > 0 and peo.locator('.custom-p').count() > 0:
                psos.append({
                    # "Title": pso.locator('.custom-h3').text_content().strip(),
                    f"Description of {pso.locator('.custom-h3').text_content().strip()}": pso.locator('.custom-p').text_content().strip()
                })
        pos = []
        po_items = page.locator('h2:text("Program Outcomes") ~ .ed-obj .ed-obj-item').all()
        for po in po_items:
            if po.locator('.custom-h3').count() > 0 and po.locator('.custom-p').count() > 0:
                pos.append({
                    # "Title": po.locator('.custom-h3').text_content().strip(),
                    f"Description of {po.locator('.custom-h3').text_content().strip()}": po.locator('.custom-p').text_content().strip()
                })
                
        section_data = {
            "Vision": vision,
            "Mission": mission_items,
            "Program_Educational_Objectives": peos,
            "Program_Specific_Outcomes": psos,
            "Program_Outcomes": pos
        }

    elif section_name == "Courses Offered":
        page.wait_for_selector('.courses-offered')
        courses = []
        
        course_items = page.locator('.course-item').all()
        for item in course_items:
            course_details = {
                "Degree": item.locator('.custom-h2').text_content().strip(),
                "Program": item.locator('.custom-h2').text_content().strip()+" "+item.locator('.custom-h3.red').first.text_content().strip()
            }

            if item.locator('.custom-h3.red').count() > 1:
                course_details["Specialization"] = item.locator('.custom-h3.red').nth(1).text_content().strip(),
                course_details["Program"] += f" with specialization in {item.locator('.custom-h3.red').nth(1).text_content().strip()}"
            courses.append(course_details)
            
        section_data = {
            "Courses offered in electronics and biomedical": courses
        }
    elif section_name == "HOD":
        page.wait_for_selector('.grid')
        page.wait_for_selector('.photo-item .person-name', state='visible')
        page.wait_for_selector('.photo-item .person-position', state='visible')

        section_data = {
            "Name of HOD": page.locator('.photo-item .person-name').text_content().strip(),
            "Position of HOD": page.locator('.photo-item .person-position').text_content().strip(),
            "Email of HOD":page.locator('.bio-contact-item a').get_attribute('href').replace('mailto:', '') if page.locator('.bio-contact-item a').count() > 0 else None,
            "Image URL of HOD": page.locator('.photo-item img').get_attribute('src'),
        }
    elif section_name == "Faculty":
        page.wait_for_selector('.grid')
        faculty_members = []
        page.wait_for_selector('.photo-item',state = 'visible')
        page.wait_for_selector('.photo-item .person-name', state='visible')
        page.wait_for_selector('.photo-item .person-position', state='visible')
        for member in page.locator('.photo-item').all():
            faculty_details = {
                "Name": member.locator('.person-name').text_content().strip(),
                "Position": member.locator('.person-position').text_content().strip(),
                "Image URL": member.locator('img').get_attribute('src')
            }
        
            # profile_link = member.locator('.custom-a').get_attribute('href')
            # if profile_link:
            #     faculty_details["Profile Link"] = profile_link
                
            faculty_members.append(faculty_details)
            
        section_data = {
            "Faculty_Members of electronics and biomedical": faculty_members
        }
    elif section_name == "Facilities":
        page.wait_for_selector('.page-content')
        
        # Get main description
        main_description = page.locator('.page-content > div > .custom-p').first.text_content().strip()
        
        # Get all facilities
        facilities = []
        for facility in page.locator('.facility-items > div').all():
            facility_details = {
                "Name": facility.locator('.custom-h3').text_content().strip(),
                f"Description of {facility.locator('.custom-h3').text_content().strip()}": facility.locator('.custom-p').text_content().strip()
            }
            facilities.append(facility_details)
            
        section_data = {
            "Main_Description of facilities offered in electronics and biomedical": main_description,
            "Facilities offered in electronics and biomedical": facilities
        }
    elif section_name == "Resources":
        page.wait_for_selector('.page-content')
        main_description = page.locator('.page-content > div > .custom-p').first.text_content().strip()
        
        resources = []
        for resource in page.locator('.res > div').all():
            resource_details = {
                # "Name": resource.locator('.custom-h3').text_content().strip(),
                f"Description of {resource.locator('.custom-h3').text_content().strip()}": resource.locator('.custom-p').text_content().strip(),
                "Links": [
                    {
                        # "Title": link.text_content().strip(),
                        # "URL ": link.get_attribute('href')
                        f"URL of {link.text_content().strip()}": link.get_attribute('href')
                    }
                    for link in resource.locator('.custom-a').all()
                ]
            }
            resources.append(resource_details)
            
        section_data = {
            "Main_Description": main_description,
            "Resources available in electronics and biomedical": resources
        }  

    elif section_name == "Associations":
        page.wait_for_selector('.asc')
        
        section_data = {
            "Name": page.locator('.asc .custom-h3').text_content().strip(),
            "Description of association in electronics and biomedical": page.locator('.asc .custom-p').text_content().strip()
        }

    elif section_name == "Achievements":
        page.wait_for_selector('.page-content')
        
        main_description = page.locator('.page-content > div > div > .custom-p').text_content().strip()
        page.wait_for_selector('.std-achievements ul > li')
        achievements = []
        c=0
        for item in page.locator('.std-achievements ul > li').all():
            achievement_text = item.inner_text().strip()
            if item.locator('b').count() > 0:
                title = item.locator('b').text_content().strip()
                if item.locator('ol').count() > 0:
                    sub_achievements = [
                        li.text_content().strip() 
                        for li in item.locator('ol > li').all()
                    ]
                    achievements.append({
                        "Title": title,
                        f"Sub_Achievements like {title}": sub_achievements
                    })
                else:
                    content = achievement_text.replace(title, '').strip()
                    achievements.append({
                        "Title": title,
                        f"{title} Description": content
                    })
            else:
                c+=1
                achievements.append({                   
                    f"Description of achievement {c}": achievement_text
                })
        section_data = {
            "Main_Description": main_description,
            "Achievements of electronics and biomedical department": achievements
        } 
    elif section_name == "Recent Projects":
        page.wait_for_selector('.page-content')
        main_description = page.locator('.page-content > div > div > .custom-p').first.text_content().strip()
        page.wait_for_selector('.project-item')
        projects = []
        for project in page.locator('.project-item').all():
            project_details = {
                # "Title": project.locator('.custom-h3').text_content().strip(),
                f"Description of {project.locator('.custom-h3').text_content().strip()}": project.locator('.custom-p').text_content().strip()
            }
            links = project.locator('a').all()
            if links:
                project_details["Links"] = [
                    {
                        # "Text": link.text_content().strip(),
                        f"URL of {link.text_content().strip()}": link.get_attribute('href')
                    }
                    for link in links
                ]
            
            projects.append(project_details)
            
        section_data = {
            "Main_Description of projects in electronics and biomedical": main_description,
            "Projects of electronics and biomedical department": projects
        }

    try:
        with open(output_file, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    
    # Update and write the data
    existing_data.update(section_data)
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    
    browser.close()

def mechanical_engineering_section(playwright,section_name, output_file="MEC.json"):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/departments/me')

    button_selector = f".sidebar-nav-li:has-text('{section_name}')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    
    section_data = {}
    if section_name == "About":
        page.wait_for_selector('.about')
        section_data = {
            "Description": page.locator('.about > .custom-p').text_content().strip()
        }
    elif section_name == "Vision & Mission":
        
        page.wait_for_selector('.vision-mission')

        vision = page.locator('.vision .custom-p').text_content().strip()

        mission_items = []
        for item in page.locator('.mission-item').all():

            paragraphs = item.locator('.custom-p').all()
            if len(paragraphs) >= 2: 
                mission_number = paragraphs[0].text_content().strip()  
                mission_text = paragraphs[1].text_content().strip()   
                mission_items.append({
                    # "Number": mission_number,
                    f"Description of mission {mission_number}": mission_text
                })
        
        peos = []
        peo_items = page.locator('h2:text("Program Educational Objectives") ~ .ed-obj .ed-obj-item').all()
        for peo in peo_items:
            if peo.locator('.custom-h3').count() > 0 and peo.locator('.custom-p').count() > 0:
                peos.append({
                    # "Title": peo.locator('.custom-h3').text_content().strip(),
                    f"Description of {peo.locator('.custom-h3').text_content().strip()}": peo.locator('.custom-p').text_content().strip()
                })

        psos = []
        pso_items = page.locator('h2:text("Program Specific Outcomes") ~ .ed-obj .ed-obj-item').all()
        for pso in pso_items:
            if pso.locator('.custom-h3').count() > 0 and peo.locator('.custom-p').count() > 0:
                psos.append({
                    # "Title": pso.locator('.custom-h3').text_content().strip(),
                    f"Description of {pso.locator('.custom-h3').text_content().strip()}": pso.locator('.custom-p').text_content().strip()
                })
        pos = []
        po_items = page.locator('h2:text("Program Outcomes") ~ .ed-obj .ed-obj-item').all()
        for po in po_items:
            if po.locator('.custom-h3').count() > 0 and po.locator('.custom-p').count() > 0:
                pos.append({
                    # "Title": po.locator('.custom-h3').text_content().strip(),
                    f"Description of {po.locator('.custom-h3').text_content().strip()}": po.locator('.custom-p').text_content().strip()
                })
                
        section_data = {
            "Vision": vision,
            "Mission": mission_items,
            "Program_Educational_Objectives": peos,
            "Program_Specific_Outcomes": psos,
            "Program_Outcomes": pos
        }

    elif section_name == "Courses Offered":
        page.wait_for_selector('.courses-offered')
        courses = []
        
        course_items = page.locator('.course-item').all()
        for item in course_items:
            course_details = {
                "Degree": item.locator('.custom-h2').text_content().strip(),
                "Program": item.locator('.custom-h2').text_content().strip()+" "+item.locator('.custom-h3.red').first.text_content().strip()
            }

            if item.locator('.custom-h3.red').count() > 1:
                course_details["Specialization"] = item.locator('.custom-h3.red').nth(1).text_content().strip(),
                course_details["Program"] += f" with specialization in {item.locator('.custom-h3.red').nth(1).text_content().strip()}"
            courses.append(course_details)
            
        section_data = {
            "Courses offered in mechanical engineering": courses
        }
    elif section_name == "HOD":
        page.wait_for_selector('.grid')
        page.wait_for_selector('.photo-item .person-name', state='visible')
        page.wait_for_selector('.photo-item .person-position', state='visible')

        section_data = {
            "Name of HOD": page.locator('.photo-item .person-name').text_content().strip(),
            "Position of HOD": page.locator('.photo-item .person-position').text_content().strip(),
            "Email of HOD":page.locator('.bio-contact-item a').get_attribute('href').replace('mailto:', '') if page.locator('.bio-contact-item a').count() > 0 else None,
            "Image URL of HOD": page.locator('.photo-item img').get_attribute('src'),
        }
    elif section_name == "Faculty":
        page.wait_for_selector('.grid')
        faculty_members = []
        page.wait_for_selector('.photo-item',state = 'visible')
        page.wait_for_selector('.photo-item .person-name', state='visible')
        page.wait_for_selector('.photo-item .person-position', state='visible')
        for member in page.locator('.photo-item').all():
            faculty_details = {
                "Name": member.locator('.person-name').text_content().strip(),
                "Position": member.locator('.person-position').text_content().strip(),
                "Image URL": member.locator('img').get_attribute('src')
            }
        
            # profile_link = member.locator('.custom-a').get_attribute('href')
            # if profile_link:
            #     faculty_details["Profile Link"] = profile_link
                
            faculty_members.append(faculty_details)
            
        section_data = {
            "Faculty_Members of mechanical engineering": faculty_members
        }
    elif section_name == "Facilities":
        page.wait_for_selector('.page-content')
        
        # Get main description
        main_description = page.locator('.page-content > div > .custom-p').first.text_content().strip()
        
        # Get all facilities
        facilities = []
        for facility in page.locator('.facility-items > div').all():
            facility_details = {
                "Name": facility.locator('.custom-h3').text_content().strip(),
                f"Description of {facility.locator('.custom-h3').text_content().strip()}": facility.locator('.custom-p').text_content().strip()
            }
            facilities.append(facility_details)
            
        section_data = {
            "Main_Description of facilities offered in mechanical engineering": main_description,
            "Facilities offered in mechanical engineering": facilities
        }
    elif section_name == "Resources":
        page.wait_for_selector('.page-content')
        main_description = page.locator('.page-content > div > .custom-p').first.text_content().strip()
        
        resources = []
        for resource in page.locator('.res > div').all():
            resource_details = {
                # "Name": resource.locator('.custom-h3').text_content().strip(),
                f"Description of {resource.locator('.custom-h3').text_content().strip()}": resource.locator('.custom-p').text_content().strip(),
                "Links": [
                    {
                        # "Title": link.text_content().strip(),
                        # "URL ": link.get_attribute('href')
                        f"URL of {link.text_content().strip()}": link.get_attribute('href')
                    }
                    for link in resource.locator('.custom-a').all()
                ]
            }
            resources.append(resource_details)
            
        section_data = {
            "Main_Description": main_description,
            "Resources available in mechanical engineering": resources
        }  

    elif section_name == "Associations":
        page.wait_for_selector('.asc')
        
        section_data = {
            "Name": page.locator('.asc .custom-h3').text_content().strip(),
            "Description of association in mechanical engineering": page.locator('.asc .custom-p').text_content().strip()
        }

    elif section_name == "Achievements":
        page.wait_for_selector('.page-content')
        
        main_description = page.locator('.page-content > div > div > .custom-p').text_content().strip()
        page.wait_for_selector('.std-achievements ul > li')
        achievements = []
        c=0
        for item in page.locator('.std-achievements ul > li').all():
            achievement_text = item.inner_text().strip()
            if item.locator('b').count() > 0:
                title = item.locator('b').text_content().strip()
                if item.locator('ol').count() > 0:
                    sub_achievements = [
                        li.text_content().strip() 
                        for li in item.locator('ol > li').all()
                    ]
                    achievements.append({
                        "Title": title,
                        f"Sub_Achievements like {title}": sub_achievements
                    })
                else:
                    content = achievement_text.replace(title, '').strip()
                    achievements.append({
                        "Title": title,
                        f"{title} Description": content
                    })
            else:
                c+=1
                achievements.append({                   
                    f"Description of achievement {c}": achievement_text
                })
        section_data = {
            "Main_Description": main_description,
            "Achievements of mechanical engineering department": achievements
        } 
    elif section_name == "Recent Projects":
        page.wait_for_selector('.page-content')
        main_description = page.locator('.page-content > div > div > .custom-p').first.text_content().strip()
        page.wait_for_selector('.project-item')
        projects = []
        for project in page.locator('.project-item').all():
            project_details = {
                # "Title": project.locator('.custom-h3').text_content().strip(),
                f"Description of {project.locator('.custom-h3').text_content().strip()}": project.locator('.custom-p').text_content().strip()
            }
            links = project.locator('a').all()
            if links:
                project_details["Links"] = [
                    {
                        # "Text": link.text_content().strip(),
                        f"URL of {link.text_content().strip()}": link.get_attribute('href')
                    }
                    for link in links
                ]
            
            projects.append(project_details)
            
        section_data = {
            "Main_Description of projects in mechanical engineering": main_description,
            "Projects of mechanical engineering department": projects
        }

    try:
        with open(output_file, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    
    # Update and write the data
    existing_data.update(section_data)
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    
    browser.close()


def applied_science_section(playwright,section_name, output_file="MEC.json"):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/departments/as')

    button_selector = f".sidebar-nav-li:has-text('{section_name}')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    
    section_data = {}
    if section_name == "About":
        page.wait_for_selector('.about')
        section_data = {
            "Description": page.locator('.about > .custom-p').text_content().strip()
        }
    elif section_name == "Vision & Mission":
        
        page.wait_for_selector('.vision-mission')

        vision = page.locator('.vision .custom-p').text_content().strip()

        mission_items = []
        for item in page.locator('.mission-item').all():

            paragraphs = item.locator('.custom-p').all()
            if len(paragraphs) >= 2: 
                mission_number = paragraphs[0].text_content().strip()  
                mission_text = paragraphs[1].text_content().strip()   
                mission_items.append({
                    # "Number": mission_number,
                    f"Description of mission {mission_number}": mission_text
                })
        
        peos = []
        peo_items = page.locator('h2:text("Program Educational Objectives") ~ .ed-obj .ed-obj-item').all()
        for peo in peo_items:
            if peo.locator('.custom-h3').count() > 0 and peo.locator('.custom-p').count() > 0:
                peos.append({
                    # "Title": peo.locator('.custom-h3').text_content().strip(),
                    f"Description of {peo.locator('.custom-h3').text_content().strip()}": peo.locator('.custom-p').text_content().strip()
                })

        psos = []
        pso_items = page.locator('h2:text("Program Specific Outcomes") ~ .ed-obj .ed-obj-item').all()
        for pso in pso_items:
            if pso.locator('.custom-h3').count() > 0 and peo.locator('.custom-p').count() > 0:
                psos.append({
                    # "Title": pso.locator('.custom-h3').text_content().strip(),
                    f"Description of {pso.locator('.custom-h3').text_content().strip()}": pso.locator('.custom-p').text_content().strip()
                })
        pos = []
        po_items = page.locator('h2:text("Program Outcomes") ~ .ed-obj .ed-obj-item').all()
        for po in po_items:
            if po.locator('.custom-h3').count() > 0 and po.locator('.custom-p').count() > 0:
                pos.append({
                    # "Title": po.locator('.custom-h3').text_content().strip(),
                    f"Description of {po.locator('.custom-h3').text_content().strip()}": po.locator('.custom-p').text_content().strip()
                })
                
        section_data = {
            "Vision": vision,
            "Mission": mission_items,
            "Program_Educational_Objectives": peos,
            "Program_Specific_Outcomes": psos,
            "Program_Outcomes": pos
        }

    elif section_name == "Courses Offered":
        page.wait_for_selector('.courses-offered')
        courses = []
        
        course_items = page.locator('.course-item').all()
        for item in course_items:
            course_details = {
                "Degree": item.locator('.custom-h2').text_content().strip(),
                "Program": item.locator('.custom-h2').text_content().strip()+" "+item.locator('.custom-h3.red').first.text_content().strip()
            }

            if item.locator('.custom-h3.red').count() > 1:
                course_details["Specialization"] = item.locator('.custom-h3.red').nth(1).text_content().strip(),
                course_details["Program"] += f" with specialization in {item.locator('.custom-h3.red').nth(1).text_content().strip()}"
            courses.append(course_details)
            
        section_data = {
            "Courses offered in applied science": courses
        }
    elif section_name == "HOD":
        page.wait_for_selector('.grid')
        page.wait_for_selector('.photo-item .person-name', state='visible')
        page.wait_for_selector('.photo-item .person-position', state='visible')

        section_data = {
            "Name of HOD": page.locator('.photo-item .person-name').text_content().strip(),
            "Position of HOD": page.locator('.photo-item .person-position').text_content().strip(),
            "Email of HOD":page.locator('.bio-contact-item a').get_attribute('href').replace('mailto:', '') if page.locator('.bio-contact-item a').count() > 0 else None,
            "Image URL of HOD": page.locator('.photo-item img').get_attribute('src'),
        }
    elif section_name == "Faculty":
        page.wait_for_selector('.grid')
        faculty_members = []
        page.wait_for_selector('.photo-item',state = 'visible')
        page.wait_for_selector('.photo-item .person-name', state='visible')
        page.wait_for_selector('.photo-item .person-position', state='visible')
        for member in page.locator('.photo-item').all():
            faculty_details = {
                "Name": member.locator('.person-name').text_content().strip(),
                "Position": member.locator('.person-position').text_content().strip(),
                "Image URL": member.locator('img').get_attribute('src')
            }
        
            # profile_link = member.locator('.custom-a').get_attribute('href')
            # if profile_link:
            #     faculty_details["Profile Link"] = profile_link
                
            faculty_members.append(faculty_details)
            
        section_data = {
            "Faculty_Members of applied science": faculty_members
        }
    elif section_name == "Facilities":
        page.wait_for_selector('.page-content')
        
        # Get main description
        main_description = page.locator('.page-content > div > .custom-p').first.text_content().strip()
        
        # Get all facilities
        facilities = []
        for facility in page.locator('.facility-items > div').all():
            facility_details = {
                "Name": facility.locator('.custom-h3').text_content().strip(),
                f"Description of {facility.locator('.custom-h3').text_content().strip()}": facility.locator('.custom-p').text_content().strip()
            }
            facilities.append(facility_details)
            
        section_data = {
            "Main_Description of facilities offered in applied science": main_description,
            "Facilities offered in applied science": facilities
        }
    elif section_name == "Resources":
        page.wait_for_selector('.page-content')
        main_description = page.locator('.page-content > div > .custom-p').first.text_content().strip()
        
        resources = []
        for resource in page.locator('.res > div').all():
            resource_details = {
                # "Name": resource.locator('.custom-h3').text_content().strip(),
                f"Description of {resource.locator('.custom-h3').text_content().strip()}": resource.locator('.custom-p').text_content().strip(),
                "Links": [
                    {
                        # "Title": link.text_content().strip(),
                        # "URL ": link.get_attribute('href')
                        f"URL of {link.text_content().strip()}": link.get_attribute('href')
                    }
                    for link in resource.locator('.custom-a').all()
                ]
            }
            resources.append(resource_details)
            
        section_data = {
            "Main_Description": main_description,
            "Resources available in applied science": resources
        }  

    elif section_name == "Associations":
        page.wait_for_selector('.asc')
        
        section_data = {
            "Name": page.locator('.asc .custom-h3').text_content().strip(),
            "Description of association in applied science": page.locator('.asc .custom-p').text_content().strip()
        }

    elif section_name == "Achievements":
        page.wait_for_selector('.page-content')
        
        main_description = page.locator('.page-content > div > div > .custom-p').text_content().strip()
        page.wait_for_selector('.std-achievements ul > li')
        achievements = []
        c=0
        for item in page.locator('.std-achievements ul > li').all():
            achievement_text = item.inner_text().strip()
            if item.locator('b').count() > 0:
                title = item.locator('b').text_content().strip()
                if item.locator('ol').count() > 0:
                    sub_achievements = [
                        li.text_content().strip() 
                        for li in item.locator('ol > li').all()
                    ]
                    achievements.append({
                        "Title": title,
                        f"Sub_Achievements like {title}": sub_achievements
                    })
                else:
                    content = achievement_text.replace(title, '').strip()
                    achievements.append({
                        "Title": title,
                        f"{title} Description": content
                    })
            else:
                c+=1
                achievements.append({                   
                    f"Description of achievement {c}": achievement_text
                })
        section_data = {
            "Main_Description": main_description,
            "Achievements of applied science department": achievements
        } 
    elif section_name == "Recent Projects":
        page.wait_for_selector('.page-content')
        main_description = page.locator('.page-content > div > div > .custom-p').first.text_content().strip()
        page.wait_for_selector('.project-item')
        projects = []
        for project in page.locator('.project-item').all():
            project_details = {
                # "Title": project.locator('.custom-h3').text_content().strip(),
                f"Description of {project.locator('.custom-h3').text_content().strip()}": project.locator('.custom-p').text_content().strip()
            }
            links = project.locator('a').all()
            if links:
                project_details["Links"] = [
                    {
                        # "Text": link.text_content().strip(),
                        f"URL of {link.text_content().strip()}": link.get_attribute('href')
                    }
                    for link in links
                ]
            
            projects.append(project_details)
            
        section_data = {
            "Main_Description of projects in applied science": main_description,
            "Projects of applied science department": projects
        }

    try:
        with open(output_file, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    
    # Update and write the data
    existing_data.update(section_data)
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    
    browser.close()


def placements_section(playwright,section_name, output_file="MEC.json"):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://www.mec.ac.in/placements')

    button_selector = f".sidebar-nav-li:has-text('{section_name}')"
    page.wait_for_selector(button_selector)
    page.click(button_selector)
    
    section_data = {}
    if section_name == "Activities":
        page.wait_for_selector('.activities')
        activities = [
            item.text_content().strip()
            for item in page.locator('.activities ul li').all()
        ]
        
        section_data = {
            "Activities of placement cell": activities
        }
    elif section_name == "Placement Statistics":
        
        page.wait_for_selector('.placement-stats')
        description = page.locator('.special_p').text_content().strip()
        years = [
            year.get_attribute('value')
            for year in page.locator('.select option').all()
        ]
        companies = []
        total = {}
        
        for row in page.locator('.Table tbody tr').all():
            # Skip the total row
            style = row.get_attribute('style')
            if style and 'background-color' in style:
                total = {
                    "CSE": row.locator('td').nth(1).text_content().strip(),
                    "EBE": row.locator('td').nth(2).text_content().strip(),
                    "ECE": row.locator('td').nth(3).text_content().strip(),
                    "EEE": row.locator('td').nth(4).text_content().strip(),
                    "Total": row.locator('td').nth(5).text_content().strip()
                }
                continue
                
            company_data = {
                "Company_Name": row.locator('.company_name').text_content().strip(),
                "Logo_URL": row.locator('.logoImage img').get_attribute('src'),
                "Placements": {
                    f"placements of {row.locator('.company_name').text_content().strip()} in CSE": row.locator('td').nth(1).text_content().strip(),
                    f"placements of {row.locator('.company_name').text_content().strip()} in EBE": row.locator('td').nth(2).text_content().strip(),
                    f"placements of {row.locator('.company_name').text_content().strip()} in ECE": row.locator('td').nth(3).text_content().strip(),
                    f"placements of {row.locator('.company_name').text_content().strip()} in EEE": row.locator('td').nth(4).text_content().strip(),
                    f"placements of {row.locator('.company_name').text_content().strip()} in Total": row.locator('td').nth(5).text_content().strip()
                }
            }
            companies.append(company_data)
            
        section_data = {
            "Description": description,
            "Available_Years": years,
            "Companies": companies,
            "Total_Placements": total
        }

    elif section_name == "Brochure":
        page.wait_for_selector('.brochure')
        page.wait_for_selector('.brochure-grid a')
        brochures = []
        for brochure in page.locator('.brochure-grid a').all():
            brochure_data = {
                # "Year": brochure.locator('img').get_attribute('alt'),
                f"PDF_URL of {brochure.locator('img').get_attribute('alt')}": brochure.get_attribute('href'),
                # "Thumbnail_URL": brochure.locator('img').get_attribute('src')
            }
            brochures.append(brochure_data)
            
        section_data = {
            "Brochures of each year": brochures
        }
    elif section_name == "Student Verification":
        page.wait_for_selector('.student-verification')
        description = page.locator('.student-verification > .custom-p').first.text_content().strip()

        requirements = [
            item.text_content().strip()
            for item in page.locator('.student-verification ul li').all()
        ]
        # signature = page.locator('.student-verification > .custom-p').nth(1).text_content().strip()

        form_link = {
            # "Text": page.locator('.student-verification .custom-h3').text_content().strip(),
            "Request form URL": page.locator('.student-verification .custom-h3').get_attribute('href')
        }
        
        section_data = {
            "Description": description,
            "Requirements": requirements,
            # "Signature": signature,
            "Form_Download": form_link
        }
    elif section_name == "Contact Details":
        page.wait_for_selector('.contact-details')

        address = []
        for item in page.locator('.contact-details > ul li').all():
            # Check if item has phone/email icon
            if item.get_attribute('class') and 'flex' in item.get_attribute('class'):
                contact_type = 'Phone' if 'Phone' in item.locator('img').get_attribute('alt') else 'Email'
                address.append({
                    "Type": contact_type,
                    "Value": item.text_content().strip().replace('\xa0', ' ').strip()
                })
            else:
                address.append({
                    "Type": "Address_Line",
                    "Value": item.text_content().strip()
                })

        # Get placement committee details
        committee = []
        page.wait_for_selector('.placement-comittee-grid-left')
        grid_left = page.locator('.placement-comittee-grid-left').all()
        page.wait_for_selector('.placement-comittee-grid-right')
        grid_right = page.locator('.placement-comittee-grid-right').all()
        
        for i in range(len(grid_left)):
            position = grid_left[i].locator('h3').text_content().strip()
            
            # Handle multiple paragraphs for student coordinators
            contact_info = {
                "Position": position,
                "Details": []
            }
            
            # Get all paragraphs in this grid section
            paragraphs = grid_right[i].locator('.custom-p').all()
            for para in paragraphs:
                text = para.text_content().strip()
                for line in text.split('\n'):
                    line = line.strip()
                    if '@' in line:  # Email
                        contact_info["Details"].append({
                            "Type": "Email",
                            "Value": line.strip()
                        })
                    elif '+91' in line:  # Phone
                        contact_info["Details"].append({
                            "Type": "Phone",
                            "Value": line.strip()
                        })
                    elif line:  # Name or designation
                        contact_info["Details"].append({
                            "Type": "Name_Or_Designation",
                            "Value": line.strip()
                        })
            
            committee.append(contact_info)
            
        section_data = {
            "Address": address,
            "Placement_Committee": committee
        }
    elif section_name == "Training Cell":
        page.wait_for_selector('.page-content')
        
        # Use more specific selector to target only the Training Cell section
        section_data = {
            # "Title": page.locator('h2:has-text("Training Cell")').text_content().strip(),
            f"Description of {page.locator('h2:has-text("Training Cell")').text_content().strip()}": page.locator('h2:has-text("Training Cell") + p.custom-p').text_content().strip()
        }
    else:
        print(f"Warning: Section '{section_name}' not recognized. No data will be scraped.")
        section_data = {
            "error": f"Section '{section_name}' not found or not supported for scraping"
        }
    try:
        with open(output_file, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    
    # Update and write the data
    existing_data.update(section_data)
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)
    
    browser.close()



with sync_playwright() as playwright:
    # scrape_principal_details(playwright)
    # scrape_about_section(playwright)
    # scrape_board_of_governors_section(playwright)
    # scrape_administrative_staff_section(playwright)
    # scrape_academic_council_section(playwright)
    # scrape_pta_section(playwright)
    # scrape_senate_section(playwright)
    # scrape_admission_details_section(playwright)
    # scrape_facilities(playwright)
    # scrape_about_statutory_committee(playwright)
    # scrape_iqac_section(playwright)
    # scrape_grievance_cell(playwright)
    # scrape_anti_ragging_committee(playwright)
    # scrape_anti_ragging_squad(playwright)
    # scrape_anti_sexual_harassment_cell(playwright)
    # scrape_safety_manual(playwright)
    # comp_sci_section(playwright,"About")
    # comp_sci_section(playwright,"Vision & Mission")
    # comp_sci_section(playwright,"Courses Offered")
    # comp_sci_section(playwright,"HOD")
    # comp_sci_section(playwright,"Faculty")
    # comp_sci_section(playwright,"Facilities")
    # comp_sci_section(playwright,"Resources")
    # comp_sci_section(playwright,"Associations")
    # comp_sci_section(playwright,"Achievements")
    # comp_sci_section(playwright,"Recent Projects")
    # electronics_and_communication_section(playwright,"About")
    # electronics_and_communication_section(playwright,"Vision & Mission")
    # electronics_and_communication_section(playwright,"Courses Offered")
    # electronics_and_communication_section(playwright,"HOD")
    # electronics_and_communication_section(playwright,"Faculty")
    # electronics_and_communication_section(playwright,"Facilities")
    # electronics_and_communication_section(playwright,"Resources")
    # electronics_and_communication_section(playwright,"Associations")
    # electronics_and_communication_section(playwright,"Achievements")
    # electronics_and_communication_section(playwright,"Recent Projects")
    # electrical_and_electronics_section(playwright,"About")
    # electrical_and_electronics_section(playwright,"Vision & Mission")
    # electrical_and_electronics_section(playwright,"Courses Offered")
    # electrical_and_electronics_section(playwright,"HOD")
    # electrical_and_electronics_section(playwright,"Faculty")
    # electrical_and_electronics_section(playwright,"Facilities")
    # electrical_and_electronics_section(playwright,"Resources")
    # electrical_and_electronics_section(playwright,"Associations")
    # electrical_and_electronics_section(playwright,"Recent Projects")
    # electronics_and_biomedical_section(playwright,"About")
    # electronics_and_biomedical_section(playwright,"Vision & Mission")
    # electronics_and_biomedical_section(playwright,"Courses Offered")
    # electronics_and_biomedical_section(playwright,"HOD")
    # electronics_and_biomedical_section(playwright,"Faculty")
    # electronics_and_biomedical_section(playwright,"Facilities")
    # electronics_and_biomedical_section(playwright,"Resources")
    # electronics_and_biomedical_section(playwright,"Associations")
    # electronics_and_biomedical_section(playwright,"Achievements")
    # electronics_and_biomedical_section(playwright,"Recent Projects")
    # mechanical_engineering_section(playwright,"About")
    # mechanical_engineering_section(playwright,"Courses Offered")
    # mechanical_engineering_section(playwright,"HOD")
    # mechanical_engineering_section(playwright,"Faculty")
    # mechanical_engineering_section(playwright,"Facilities")
    # mechanical_engineering_section(playwright,"Resources")
    # applied_science_section(playwright,"About")
    # applied_science_section(playwright,"HOD")
    # applied_science_section(playwright,"Faculty")
    # applied_science_section(playwright,"Resources")
    placements_section(playwright,"Activities")
    placements_section(playwright,"Placement Statistics")
    placements_section(playwright,"Brochure")
    placements_section(playwright,"Student Verification")
    placements_section(playwright, "Contact Details")
    placements_section(playwright,"Training Cell")