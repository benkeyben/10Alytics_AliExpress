## Project Title - Building and Managing ETL Data Pipeline for Laptop Data at AliExpress website
  ### Author - Benjamin Yankey 
  
  ### Project Description: 
  Embark on a challenging journey with this project, where I was tasked to tackle the extraction of a substantial and diverse dataset from the AliExpress website and its API. The primary focus revolves around addressing complexities, variabilities, and ethical considerations associated with efficient and accurate data scraping. Furthermore, I aim to transform the extracted data into a structured format conducive to thorough analysis. The core objective is the development of a reliable, scalable pipeline that supports routine data updates and maintenance. 
  Key tasks include 
  - scraping data without disrupting the website's operations.
  - cleaning and normalizing extracted data for quality assurance.
  - transforming data into optimized tables for enhanced query performance and integrity.
  - loading the refined data into a PostgreSQL database, ensuring adherence to data security and governance standards.
  This project aims to create a scalable and maintainable system capable of accommodating future changes in data sources and structures.

### Project Workflow Chart
  <img src="images/ALiExpress_Flow_Chart.jpg" alt="AliExpress flow chart" width="500"/>

### Project Entity Relationship Diagram Chart
  <img src="images/ALIEXPRESS ERD.jpg" alt="AliExpress ERD" width="500"/>

### Project Tools and Technologies
  - ### Data Extraction:
    *  Python libraries
       * Requests for sending and receiving  HTTP requests. 
       * BeautifulSoup for web scrapping to extract data from the AliExpress website and its API
  - ### Data Cleaning and Transformation:
    * Python library - Pandas for cleaning and transforming data into csv files.
  
  - ### Data Loading and storage:
    * Postgresql to receive and store structured data.
    * SQL for data manipulation, transformation, and querying within the PostgreSQL environment.
      
  - ### Maintenance and Scaling
    * Normalization technique used in creating tables in database to ensure scalability of databse.
      
  - ### Documentation of the entire process for future reference and modification.
    * README.md file
    * Employed code comments to explain complex logic, transformations, or any parts of the code that might not be immediately obvious
    * Employed logging to capture important events, errors, and information during the pipeline execution.
    * The use of git version control maintaining clear commit messages to track changes and improvements.
    
  - ### Data Sources:
    * AliExpress API and AliExpress website, which provide a rich source of e-commerce data.
### Project Challenges
  - Error Handling and Logging: I encounted diverse error types such as data inconsistencies and format discrepancies.
  - Handling Schema Changes: Changes in source data schemas or unexpected changes in data formats can result in errors during the ETL process.
  - Testing: This was time consumming as I had to test individual components of the ETL process, such as functions or methods responsible for extraction, transformation, and loading.
### Project Recommendation
  - Handling Error Handling and Logging:
    * Centralized Logging: Implement a centralized logging system that captures logs from different components of your ETL process.
      This makes it easier to trace and troubleshoot errors.

    * Detailed Error Messages: Ensure that your error messages are informative and detailed. Include information about the nature of
      the error, the affected data, and the location within the ETL process where the error occurred.

    * Alerting Mechanism: Implement an alerting mechanism to notify the relevant personnel when errors occur. This could be through email alerts, 
      Slack notifications, or other communication channels.

    * Error Classification: Classify errors based on severity and type. This can help prioritize the resolution of critical issues and provide 
      insights into common problems that may need preventive measures.

  - Handling Schema Changes:
    * Schema Versioning: Implement schema versioning to manage changes in source data schemas. This allows your ETL process to adapt to schema 
      changes without causing errors.

    * Schema Validation: Include schema validation checks as part of your ETL process. This ensures that the incoming data adheres to the
      expected schema, reducing the chances of errors due to unexpected changes.

    * Metadata Management: Maintain metadata about the source data schemas and changes. This can help in dynamically adapting the ETL process
      based on the discovered schema changes.

  - Testing:
    * Automated Testing: Invest in automated testing for your ETL process. Create unit tests, integration tests, and end-to-end tests to verify
      the correctness of each component and the entire ETL pipeline.

    * Mock Data: Use mock data for testing purposes. This allows you to simulate various scenarios and conditions without relying on actual 
      production data.

    * Regression Testing: Implement regression testing to ensure that new changes or updates do not introduce new issues or break existing 
      functionality.

    * Continuous Integration (CI) and Continuous Deployment (CD): Set up CI/CD pipelines to automate the testing and deployment processes.
      This helps in quickly identifying and resolving issues during development.

    * Documentation: Document the testing procedures and expected outcomes. This documentation can be valuable for future reference and for 
      onboarding new team members.




