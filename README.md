# India Coronavirus Tracker Api

Provides data about Coronavirus outbreak in India. Includes number of confirmed cases that involve Indian nationals and confirmed cases that involve foreign nationals, Cured/Dischared/Migrated number and the number of Deaths.

## Available data-sources
*  This API collects data direclty from  [Ministry of Health and Family Welfare](https://www.mohfw.gov.in/)

## API Reference

All endpoints are located at https://dsd7azv2bl.execute-api.ap-south-1.amazonaws.com/production and are accessible via https. For instance: you can get data per state by using this URL: https://dsd7azv2bl.execute-api.ap-south-1.amazonaws.com/production/data

You can open the URL in your browser to further inspect the response or you can make this curl call in your terminal to see the prettified response:

`curl https://dsd7azv2bl.execute-api.ap-south-1.amazonaws.com/production/data | json_pp`

## API Endpoints

### Data Endpoint

`GET /data`

#### Sample response

```
"Andaman and Nicobar Islands": {
    "cured_or_discharged_or_migrated": "0",
    "death": "0",
    "helpline": "03192-232102",
    "total_confirmed_cases_foreign_national": "0",
    "total_confirmed_cases_indian_national": "1"
},
...
```

#### Response definitions

| Response Item | Description | Type |
| ------ | ------ | ------ |
| India_coronavirus | The parent key that contains all affected states | Object |
| {state} | The state key that contains the data of that affected state | Object |
| total_confirmed_cases_indian_national | The number of Indian Nationals who have been confirmed | String |
| total_confirmed_cases_foreign_national | The number of Foreign Nationals who have been confirmed | String |
| cured_or_discharged_or_migrated | The number of People who have been Cured/Discharged/Migrated | String |
| death | The number of People who have Died | String |
| helpline | The helpline number of that affected state | String |

### Helplines Endpoint

`GET /`

#### Sample response

```
helplines": {
    "Andaman and Nicobar Islands": "03192-232102",
    "Andhra Pradesh": "0866-2410978",
    "Arunachal Pradesh": "9436055743",
    "Assam": "6913347770",
    "Bihar": "104",
    ...
}
```

## Maintenance

Since this API relies upon data that is scraped from an HTML table, there are sometimes code changes that need to be done based on the structural changes done on the website

## Development Requirements

-  Python (3.8)
-  Flask

## Disclaimer

This data is provided to the public strictly for educational and academic research purposes. The API relies upon publicly available data from single or multiple sources, that do not always agree. We hereby disclaim any and all representations and warranties with respect to the API, including accuracy, fitness for use, and merchantability. Reliance on the API for medical guidance or use of the API in commerce is strictly prohibited.

## License

See [LICENSE](LICENSE) for the license. Please link to this repo somewhere in your project :)

