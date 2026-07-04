# Database View

## users

|id|name|email|password|role|
|---|---|---|---|---|
|1|TechCorp Inc|hr@techcorp.com|scrypt:32768:8:1$LBkhMrBpHBBqLY4d$bf2ba2dcfce0f82f689fe13126f45409cb7840dcd60d0906482b8e2b1077945c872c5dcbaa4bf5880863b7704aa1f97e3363d292f4dde3791d75e23e4c634c85|employer|
|2|Sarah Jenkins|sarah@example.com|scrypt:32768:8:1$pdiZlzQfSObIJcRS$3d01e8e2116ba0ab82e9dad71fcfe9bc740b6db712f68fe359ba718f3f9de09ad7b56325a49049c15a0191188490d9922324cd01659506fce67ae167b00b5473|seeker|
|3|Ravi Kumar|ravi@example.com|scrypt:32768:8:1$pdiZlzQfSObIJcRS$3d01e8e2116ba0ab82e9dad71fcfe9bc740b6db712f68fe359ba718f3f9de09ad7b56325a49049c15a0191188490d9922324cd01659506fce67ae167b00b5473|seeker|
|4|Priya Sharma|priya@example.com|scrypt:32768:8:1$pdiZlzQfSObIJcRS$3d01e8e2116ba0ab82e9dad71fcfe9bc740b6db712f68fe359ba718f3f9de09ad7b56325a49049c15a0191188490d9922324cd01659506fce67ae167b00b5473|seeker|
|5|DataWorks Analytics|careers@dataworks.com|scrypt:32768:8:1$LBkhMrBpHBBqLY4d$bf2ba2dcfce0f82f689fe13126f45409cb7840dcd60d0906482b8e2b1077945c872c5dcbaa4bf5880863b7704aa1f97e3363d292f4dde3791d75e23e4c634c85|employer|
|6|Global Finance Solutions|recruiting@globalfinance.com|scrypt:32768:8:1$LBkhMrBpHBBqLY4d$bf2ba2dcfce0f82f689fe13126f45409cb7840dcd60d0906482b8e2b1077945c872c5dcbaa4bf5880863b7704aa1f97e3363d292f4dde3791d75e23e4c634c85|employer|


## jobs

|id|title|company|category|skills|experience|salary|location|description|last_date|employer_id|
|---|---|---|---|---|---|---|---|---|---|---|
|1|Junior Python Developer|TechCorp Inc|IT / Software|Python, Flask, SQL|1-2 Years|₹6,00,000 - ₹8,00,000|Remote|We are looking for a Junior Python developer to join our backend team to build scalable APIs.|2025-12-31|1|
|2|Frontend React Engineer|TechCorp Inc|IT / Software|React, JavaScript, CSS|3+ Years|₹12,00,000 - ₹15,00,000|Bengaluru, Karnataka|Looking for an experienced React developer to build modern and responsive UI components.|2025-11-15|1|
|3|Data Scientist|DataWorks Analytics|IT / Software|Python, Machine Learning, SQL|2-5 Years|₹10,00,000 - ₹18,00,000|Remote|Looking for an innovative data scientist to build predictive models.|2025-10-01|5|
|4|Financial Analyst|Global Finance Solutions|Finance|Excel, Financial Modeling, Accounting|1-3 Years|₹8,00,000 - ₹12,00,000|Mumbai, Maharashtra|We need a detail-oriented financial analyst to join our expanding team.|2025-12-01|6|
|5|Cloud Architect|TechCorp Inc|IT / Software|AWS, Azure, Kubernetes|7+ Years|₹20,00,000 - ₹30,00,000|Hybrid|Architect cloud infrastructure for high-traffic applications.|2025-10-15|1|
|6|QA Engineer|TechCorp Inc|IT / Software|Selenium, Cypress, Python|2-4 Years|₹8,00,000 - ₹12,00,000|Pune, Maharashtra|Ensure the quality of software releases through automated testing.|2025-09-30|1|
|7|Data Engineer|DataWorks Analytics|IT / Software|Spark, Hadoop, Python|3-5 Years|₹15,00,000 - ₹22,00,000|Bengaluru, Karnataka|Develop and maintain data pipelines for large scale analytics.|2025-11-20|5|
|8|BI Analyst|DataWorks Analytics|Analytics|Tableau, PowerBI, SQL|1-3 Years|₹6,00,000 - ₹10,00,000|Hyderabad, Telangana|Create insightful dashboards for business stakeholders.|2025-12-10|5|
|9|Risk Manager|Global Finance Solutions|Finance|Risk Management, Compliance|5-8 Years|₹18,00,000 - ₹25,00,000|Mumbai, Maharashtra|Oversee enterprise risk and ensure regulatory compliance.|2025-11-05|6|
|10|Quantitative Analyst|Global Finance Solutions|Finance|Python, C++, Statistics|2-4 Years|₹15,00,000 - ₹20,00,000|Remote|Develop algorithmic trading models.|2025-10-31|6|


## applications

|id|job_id|seeker_id|resume|status|applied_date|
|---|---|---|---|---|---|
|10|1|2|dummy_resume_sarah.pdf|Pending|2026-04-09 06:11:26|
|11|1|3|dummy_resume_ravi.pdf|Accepted|2026-04-09 06:11:26|
|12|2|4|dummy_resume_priya.pdf|Rejected|2026-04-09 06:11:26|
|13|3|2|dummy_resume_sarah.pdf|Pending|2026-04-09 06:11:26|
|14|7|3|dummy_resume_ravi.pdf|Accepted|2026-04-09 06:11:26|
|15|4|4|dummy_resume_priya.pdf|Pending|2026-04-09 06:11:26|


## seeker_profiles

|id|user_id|phone|address|skills|education|experience|
|---|---|---|---|---|---|---|
|4|2|+91 98765 43210|Mumbai, Maharashtra|Python, Flask, JavaScript, SQL|BSc Computer Science|2 years of backend web development.|


