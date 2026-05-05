---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Machine Learning + Data"
themes: ["AI ML", "Observability", "Storage Data"]
speakers: ["Vigith Maurice", "Amit Kalamkar", "Intuit"]
sched_url: https://kccnceu2023.sched.com/event/1HyZX/intuits-customer-centric-observability-journey-using-aiops-vigith-maurice-amit-kalamkar-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Intuit%E2%80%99s+Customer+Centric+Observability+Journey+Using+AIOps+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Intuit’s Customer Centric Observability Journey Using AIOps - Vigith Maurice & Amit Kalamkar, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Observability]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Vigith Maurice, Amit Kalamkar, Intuit
- Schedule: https://kccnceu2023.sched.com/event/1HyZX/intuits-customer-centric-observability-journey-using-aiops-vigith-maurice-amit-kalamkar-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Intuit%E2%80%99s+Customer+Centric+Observability+Journey+Using+AIOps+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Intuit’s Customer Centric Observability Journey Using AIOps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyZX/intuits-customer-centric-observability-journey-using-aiops-vigith-maurice-amit-kalamkar-intuit
- YouTube search: https://www.youtube.com/results?search_query=Intuit%E2%80%99s+Customer+Centric+Observability+Journey+Using+AIOps+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=D-eQxDBbx48
- YouTube title: Intuit’s Customer Centric Observability Journey Using AIOps - Vigith Maurice & Amit Kalamkar, Intuit
- Match score: 0.843
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/intuits-customer-centric-observability-journey-using-aiops/D-eQxDBbx48.txt
- Transcript chars: 22226
- Keywords: platform, observability, developer, source, anomaly, operational, analytics, interaction, search, architecture, information, little, metrics, dependency, anomalies, meaning, processing, intuit

### Resumo baseado na transcript

good afternoon everyone how is everyone doing uh my name is Amit kalamkar I lead observation analytics at Intuit I have with me widget Morris he is a principal engineer at my team and today we wanted to talk about intuit's observability Journey using a Ops here is the agenda for today first we will talk a little bit about Intuit our observability strategy then we have a live demo where we can show how this observative strategy is in action then widget will go over architecture and details on uh we pretty much modernized everything front-end back-end all this boxes you see there we also created paved roads both for containerized as well as serverless app this ensured that our developer have end-to-end automation from deployment build uh as well as scale management as part of this modernization we deliberately make and made an effort to instrument everything out of box so we get real-time events and metrics from the whole layers of our infrastructures and platform and we stored that in our operational database we also have a

### Excerpt da transcript

good afternoon everyone how is everyone doing uh my name is Amit kalamkar I lead observation analytics at Intuit I have with me widget Morris he is a principal engineer at my team and today we wanted to talk about intuit's observability Journey using a Ops here is the agenda for today first we will talk a little bit about Intuit our observability strategy then we have a live demo where we can show how this observative strategy is in action then widget will go over architecture and details on how we are achieving it and lastly we can do question and answers should know into it in from our Flagship products like Turbo Tax QuickBooks MailChimp Credit Karma Etc we are one of the largest uh SAS company out there these on the top you can see these are the five main platform areas within Intuit that powers all these products this ensures that we provide value to our customers as well as we accelerate Innovations on the bottom you can see the scale at which we operate we operate at with the large scale me and widget both belong to developer experience and platform our group provides all the platforms infrastructure and capabilities that are needed by these products uh to develop as well as operate we also run at a very large scale for example we are around 1 million CPU cores and the investment which we have done in these platforms have resulted in 6X Improvement in development velocity since 2019.

into it is very much believing a believer in open source we not only use it but we also contribute lot of things back into it is proud recipient of cncf end user award both in 2019 and 2022 into it also has created an Open Source Products uh like Argo as and Numa flow oduma product recently into it also has a lot of contributors as well as mentors in different open source projects so we are very much into open source and we want to ensure that we give back to community so now let me start with you just giving a high level idea of our platform at into it so if you look at the slide this is our modern SAS platform so we started the modernization uh in 2018. uh we pretty much modernized everything front-end back-end all this boxes you see there we also created paved roads both for containerized as well as serverless app this ensured that our developer have end-to-end automation from deployment build uh as well as scale management as part of this modernization we deliberately make and made an effort to instrument everything out of box so we get real-time events and metrics
