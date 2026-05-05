---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["Observability", "Storage Data"]
speakers: ["Robert Pająk", "Splunk"]
sched_url: https://kccncna2025.sched.com/event/27FbP/opentelemetry-logs-driving-a-major-shift-events-richer-data-and-smarter-semantics-robert-pajak-splunk
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry+Logs+Driving+a+Major+Shift%3A+Events%2C+Richer+Data%2C+and+Smarter+Semantics+CNCF+KubeCon+2025
slides: []
status: parsed
---

# OpenTelemetry Logs Driving a Major Shift: Events, Richer Data, and Smarter Semantics - Robert Pająk, Splunk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Storage Data]]
- País/cidade: United States / Atlanta
- Speakers: Robert Pająk, Splunk
- Schedule: https://kccncna2025.sched.com/event/27FbP/opentelemetry-logs-driving-a-major-shift-events-richer-data-and-smarter-semantics-robert-pajak-splunk
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry+Logs+Driving+a+Major+Shift%3A+Events%2C+Richer+Data%2C+and+Smarter+Semantics+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre OpenTelemetry Logs Driving a Major Shift: Events, Richer Data, and Smarter Semantics.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FbP/opentelemetry-logs-driving-a-major-shift-events-richer-data-and-smarter-semantics-robert-pajak-splunk
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry+Logs+Driving+a+Major+Shift%3A+Events%2C+Richer+Data%2C+and+Smarter+Semantics+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-j6bHtUV3IA
- YouTube title: OpenTelemetry Logs Driving a Major Shift: Events, Richer Data, and Smarter Semantics - Robert Pająk
- Match score: 1.006
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/opentelemetry-logs-driving-a-major-shift-events-richer-data-and-smarte/-j6bHtUV3IA.txt
- Transcript chars: 23013
- Keywords: logs, basically, attributes, events, record, logging, semantics, structured, complex, everyone, structure, create, metrics, libraries, question, presentation, solutions, native

### Resumo baseado na transcript

I'm happy that you're here that you're not you have not left the conference yet because it's pretty late. I'm Robert Pyong and basically this talk will be about open logs in open telemetry about how basically logs are becoming the first place class first place cities in open telemetry. Okay, I'll be good for you and we'll skip the slide for you because almost everyone already knows that open telemetry is open standard for generating telemetry data traces, metrics, logs and profiles are coming. What is an event and the APIs in open telemetry for logging and basically will this I will discuss how basically logs will are changing from a legacy baggage to something which is a first class citizen open telemetry. Okay question to you who has seen logs like this honestly I need your help. So do you see the passwords in in the logs like you know this like editing thing to find it easier like I I think everyone was there right but is it something that is it a place that you want to be eventually like

### Excerpt da transcript

Hello everyone. I'm happy that you're here that you're not you have not left the conference yet because it's pretty late. So welcome. I'm Robert Pyong and basically this talk will be about open logs in open telemetry about how basically logs are becoming the first place class first place cities in open telemetry. So first of all a few words about myself. I traveled from Krakco. It it's a journey enough for me. So this talk won't be about a journey about I don't know Sam or Logly or something. It will be just about it will be a present normal present regular presentation. You can find me as paret on GitHub. I used to create a lot of PRs and a lot of comments pull requests. Uh I'm hired by Splunk a Cisco company but most of my time like 90% I basically working on open source. I'm very grateful for my employer that I am I am able to create solutions that work for everyone. Yeah. And basically I'm an open telemetry go maintainer so I drink open telemetry and I'm contributing to openly logs like for two years already.

And the disclaimer I'm not an native English speaker but if something is not clear don't blame my language. It simply means that I have no idea what I'm talking about. So usually when people are you know describing some things they talk about the past, present, future. So what to have a good a good story? But honestly speaking during technology presentations who cares about the past? Let's just talk about the present and the future. Okay. So first of all I have a question to you. Who knows what is open telemetry? Okay, I'll be good for you and we'll skip the slide for you because almost everyone already knows that open telemetry is open standard for generating telemetry data traces, metrics, logs and profiles are coming. Okay. So a few sentences about the structure of this presentation. Uh first I will take about the data model of logs the open telemetry. So what is or log basically in data made in open telemetry? What are semantics? So what does it mean uh that there's a log and how is it structured?

What is an event and the APIs in open telemetry for logging and basically will this I will discuss how basically logs will are changing from a legacy baggage to something which is a first class citizen open telemetry. Okay question to you who has seen logs like this honestly I need your help. Yeah I haven't seen like this. So do you see the passwords in in the logs like you know this like editing thing to find it easier like I I think everyone was
