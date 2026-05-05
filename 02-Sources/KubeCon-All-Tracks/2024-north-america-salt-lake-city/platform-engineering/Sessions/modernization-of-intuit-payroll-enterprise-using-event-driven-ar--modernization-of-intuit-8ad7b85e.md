---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Hema Maarimuthu", "Vigith Maurice", "Intuit"]
sched_url: https://kccncna2024.sched.com/event/1i7qy/modernization-of-intuit-payroll-enterprise-using-event-driven-architecture-hema-maarimuthu-vigith-maurice-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Modernization+of+Intuit+Payroll+Enterprise+Using+Event+Driven+Architecture+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Modernization of Intuit Payroll Enterprise Using Event Driven Architecture - Hema Maarimuthu & Vigith Maurice, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Salt Lake City
- Speakers: Hema Maarimuthu, Vigith Maurice, Intuit
- Schedule: https://kccncna2024.sched.com/event/1i7qy/modernization-of-intuit-payroll-enterprise-using-event-driven-architecture-hema-maarimuthu-vigith-maurice-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Modernization+of+Intuit+Payroll+Enterprise+Using+Event+Driven+Architecture+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Modernization of Intuit Payroll Enterprise Using Event Driven Architecture.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qy/modernization-of-intuit-payroll-enterprise-using-event-driven-architecture-hema-maarimuthu-vigith-maurice-intuit
- YouTube search: https://www.youtube.com/results?search_query=Modernization+of+Intuit+Payroll+Enterprise+Using+Event+Driven+Architecture+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ukCLEYs2v5A
- YouTube title: Modernization of Intuit Payroll Enterprise Using Event Driven Architect... H. Maarimuthu, V. Maurice
- Match score: 0.961
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/modernization-of-intuit-payroll-enterprise-using-event-driven-architec/ukCLEYs2v5A.txt
- Transcript chars: 22178
- Keywords: source, pipeline, vertex, processing, write, payroll, create, platform, application, messages, message, custom, running, support, systems, scaling, complex, deploy

### Resumo baseado na transcript

good afternoon everyone our topic today is modernization of intute online payroll using even driven architecture I'm himma marim Mutu principal software engineer on the intute online payroll team leading operational excellence and security viget is here with me today he's the principal software engineer for Numa Pro if you haven't heard of intute intute is a Global Financial technology company that's building an AI native development platform that's 100 million customers across various Brands Turbo Tax Credit karmma QuickBooks and mail chimp we are really excited to be here lot of different traffic patterns that come in and we need to minimize cost as much as we can uh and the auto scaler is a custom auto scaler which just Q depth analysis we do support HP and data if need be but our default Auto scaler is capable of doing Zer to me and lastly it runs on very less uh resource footprint now this is our uh project uh if you want you can scan this is the link to Numa flow uh that's all I we do you have a Helm chart or kubernetes operator to install Numa flow I see that it's having like we have to use the cube CTL but is there no we do have help chart uh we do have there you go help ch and

### Excerpt da transcript

good afternoon everyone our topic today is modernization of intute online payroll using even driven architecture I'm himma marim Mutu principal software engineer on the intute online payroll team leading operational excellence and security viget is here with me today he's the principal software engineer for Numa Pro if you haven't heard of intute intute is a Global Financial technology company that's building an AI native development platform that's 100 million customers across various Brands Turbo Tax Credit karmma QuickBooks and mail chimp we are really excited to be here at cucon this year as we are big users of open- source tooling and have a commitment of giving back to the open source Community a little bit more about our platform our AI native development platform is massive in scale and supports over 4 million models running in production every other day has helped 8X developer velocity over the past 4 years and Powers 60 billion machine learning predictions and 40 million aops inferences per day one of the most exciting Parts about working at inth is how much open source software we use to build a development platform we are proud to be the recipients of the end user award from the cloud native Computing foundation in 2019 and 2022 and we are proud to create an open source many projects here here at in like Argo which I'm sure many of you know and the one that we are about to present the numo pro now let's move into the core part of the presentation how Numa flow helped QuickBooks Online payroll enhance the even driven architecture let's quickly take a look at how QuickBooks Online payroll supports our small business customers to understand the importance of how numof flow helped us from payroll to time tracking and HR to benefits our team management software grows with the small business team and their needs trusted payroll from Payday to tax time meaning set payroll to a schedule and get payroll taxes done for you 100% Accurate Tax calculations guaranteed your team can track their own hours making it easy to manage time sheets projects and schedules from anywhere helps grow your team with HR Support and offer affordable employee benefit s to help your team grow with you considering all of the points discussed it's evident how crucial it is for this application to be fully available scalable and to operate with high efficiency and resilience here are the challenges we faced with the Eventing systems we were not able to optimize cost effectively a
