---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Observability"
themes: ["Observability"]
speakers: ["Vinit Samel", "Intuit", "Nagaraja Tantry", "Intui"]
sched_url: https://kccncna2022.sched.com/event/182Fz/customer-centric-observability-how-intuit-reduced-time-to-detect-customer-impact-from-30+-minutes-to-under-3-minutes-vinit-samel-intuit-nagaraja-tantry-intui
youtube_search_url: https://www.youtube.com/results?search_query=Customer+Centric+Observability%3A+How+Intuit+Reduced+Time+To+Detect+Customer+Impact+From+30%2B+Minutes+To+Under+3+Minutes.+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Customer Centric Observability: How Intuit Reduced Time To Detect Customer Impact From 30+ Minutes To Under 3 Minutes. - Vinit Samel, Intuit & Nagaraja Tantry, Intui

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Detroit
- Speakers: Vinit Samel, Intuit, Nagaraja Tantry, Intui
- Schedule: https://kccncna2022.sched.com/event/182Fz/customer-centric-observability-how-intuit-reduced-time-to-detect-customer-impact-from-30+-minutes-to-under-3-minutes-vinit-samel-intuit-nagaraja-tantry-intui
- Busca YouTube: https://www.youtube.com/results?search_query=Customer+Centric+Observability%3A+How+Intuit+Reduced+Time+To+Detect+Customer+Impact+From+30%2B+Minutes+To+Under+3+Minutes.+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Customer Centric Observability: How Intuit Reduced Time To Detect Customer Impact From 30+ Minutes To Under 3 Minutes..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Fz/customer-centric-observability-how-intuit-reduced-time-to-detect-customer-impact-from-30+-minutes-to-under-3-minutes-vinit-samel-intuit-nagaraja-tantry-intui
- YouTube search: https://www.youtube.com/results?search_query=Customer+Centric+Observability%3A+How+Intuit+Reduced+Time+To+Detect+Customer+Impact+From+30%2B+Minutes+To+Under+3+Minutes.+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=b6m4Kk1z-24
- YouTube title: Customer Centric Observability: How Intuit Reduced Time To Detect... - Vinit Samel & Nagaraja Tantry
- Match score: 0.795
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/customer-centric-observability-how-intuit-reduced-time-to-detect-custo/b6m4Kk1z-24.txt
- Transcript chars: 26072
- Keywords: interaction, customer, specific, backend, engineer, experience, products, actually, trace, metrics, interactions, sampling, multiple, impact, important, provide, information, journey

### Resumo baseado na transcript

hey everyone thank you for joining us this evening I realize it's past 5:00 p.m. on a Thursday and we're all here so thank you again for that so today we are here to share our journey about customer Centric observability and how at into it we've been able to successfully detect customer impact in under 3 minutes I'm sure

### Excerpt da transcript

hey everyone thank you for joining us this evening I realize it's past 5:00 p.m. on a Thursday and we're all here so thank you again for that so today we are here to share our journey about customer Centric observability and how at into it we've been able to successfully detect customer impact in under 3 minutes I'm sure most of you are familiar with in and what it does our mission is to power Prosperity around the world with our products like Turbo Tax Credit k Mark QuickBooks and MailChimp and Behind these products there are five major platforms that enable and accelerate Innovation and enable consistency across all of these products and as you can see looking at these numbers the scale that we work with is enormous the organization that I and Naga are part of is devx and our job is to build the plat platforms and tools that enable our developers to deliver products faster and operate them excellently I'm vinit samel group Dev manager at in and I'm here with Naga a principal engineer as you may be familiar we have received the cncf award this year again and we grateful for that and we are both active contributors as well as maintainers of Open Source projects so let's take a step back on our journey so when we started our journey we were largely focused on system Centric monitoring what that means is across the thousands of services and the hundreds of web apps plugins and widgets that we have across into it each one of these components had their own way of monitoring and measuring their availability but when any of these components had an outage we lacked an understanding of customer impact our time to detect these problems was also extremely high after detecting the problem isolating this problem to the specific experiences that I have gone down the experiences that are unavailable and how do you actually recover from this problem how do you root cause how do you repair took even longer all in all at our scale we were spending a ton of dollars but not necessarily getting the best Roi on observability and most importantly we realize that we were not leveraging our own data so we took a step back and we anchored around one of our core values at into it which is customer Obsession what that means is we fall in love with our customers problems and then we sweat every detail of the experience to deliver Excellence now when you look at observability we see it's no different so while focusing on our systems is very important focusing on what customers are exp
