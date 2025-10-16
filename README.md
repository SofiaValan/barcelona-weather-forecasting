# Barcelona Weather Forecasting

## Goal

This project aims to build a regional drought forecasting system for Barcelona (Spain), leveraging meteorological data from multiple weather stations. The goal is to predict drought conditions several months in advance using historical temperature, precipitation, and climate indices.

This project is designed as a learning vehicle for mastering:

* Time series forecasting techniques (statistical and machine learning models)
* Spatial-temporal data integration and analysis
* Drought index calculation (e.g., SPI, SPEI)
* Scalable data ingestion and preprocessing pipelines
* Model deployment
* Interactive data app with Streamlit

## Context

Barcelona experienced severe droughts from 2022-2024, causing water shortages and economic impacts. Early and accurate drought prediction can help regional authorities and communities make informed water management decisions. This project explores the ability to forecast drought onset and severity using a network of weather stations to capture spatial variations.

## Dataset
This project pulls meteorological data from the Meteocat (Catalonian Weather Service) OpenData API on a daily basis. Access to the API requires:

* Free registration at https://apidocs.meteocat.gencat.cat/
* Personal API key obtained after registration. This needs manual approval.

## Milestones

* Ingest historical daily weather data from multiple stations across Barcelona via MeteoCat OpenData API
* Calculate standardized drought indices like SPI and SPEI at different time scales
* Implement various forecasting models including ARIMA, Random Forest, and LSTM neural networks
* Support multi-station spatial analysis and feature engineering
* Deploy trained models using Kubernetes for scalable drought forecasting
* Provide an interactive data app to evaluate drought periods

## Bibliography
* Barcelona Drought Impact: https://www.barcelonatravelhacks.com/hacks/info/barcelona-2024-drought
* Catalonia lifts the exceptional measures due to drought in the Barcelona region: https://www.lavanguardia.com/mediterranean/20240618/9741616/catalonia-government-lifts-exceptional-measures-drought-barcelona-water-sau-ter-llobregat.html
