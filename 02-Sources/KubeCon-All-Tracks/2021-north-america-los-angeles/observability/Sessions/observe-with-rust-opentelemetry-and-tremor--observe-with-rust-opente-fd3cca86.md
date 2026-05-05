---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Observability"
themes: ["AI ML", "Observability"]
speakers: ["Gary White Jr.", "Wayfair"]
sched_url: https://kccncna2021.sched.com/event/lV1l/observe-with-rust-opentelemetry-and-tremor-gary-white-jr-wayfair
youtube_search_url: https://www.youtube.com/results?search_query=Observe+with+Rust%3A+OpenTelemetry+and+Tremor+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Observe with Rust: OpenTelemetry and Tremor - Gary White Jr., Wayfair

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: United States / Los Angeles
- Speakers: Gary White Jr., Wayfair
- Schedule: https://kccncna2021.sched.com/event/lV1l/observe-with-rust-opentelemetry-and-tremor-gary-white-jr-wayfair
- Busca YouTube: https://www.youtube.com/results?search_query=Observe+with+Rust%3A+OpenTelemetry+and+Tremor+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Observe with Rust: OpenTelemetry and Tremor.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1l/observe-with-rust-opentelemetry-and-tremor-gary-white-jr-wayfair
- YouTube search: https://www.youtube.com/results?search_query=Observe+with+Rust%3A+OpenTelemetry+and+Tremor+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RI9cy8OJQmY
- YouTube title: Observe with Rust: OpenTelemetry and Tremor - Gary White Jr., Wayfair
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/observe-with-rust-opentelemetry-and-tremor/RI9cy8OJQmY.txt
- Transcript chars: 21964
- Keywords: tremor, signals, infrastructure, together, application, metrics, observability, understand, presentation, allows, processing, unstructured, important, logs, frameworks, collector, definition, applications

### Resumo baseado na transcript

good evening cubecon 6pm on a wednesday uh if you're hearing my voice i hope that you're here to learn about observing with rust open telemetry and tremor i am gary white jr i work for wayfair technology in the open source program office you can see me here both in my emoji form and in my true form in the corner i know that it's going to be hard to keep track of who's who the resemblance is completely perfect some of my most notable contributions to wayfarer include

### Excerpt da transcript

good evening cubecon 6pm on a wednesday uh if you're hearing my voice i hope that you're here to learn about observing with rust open telemetry and tremor i am gary white jr i work for wayfair technology in the open source program office you can see me here both in my emoji form and in my true form in the corner i know that it's going to be hard to keep track of who's who the resemblance is completely perfect some of my most notable contributions to wayfarer include my time working on tremor my time building stuff for build kite for the company including ci infrastructure and contributing to the build kite agent which is on github and of course making emojis i have literally hundreds of emojis in the waiver slack channel that spin spinning monkey is one of them and i'm very proud of it while we're talking about emojis let's go through some of the best i've curated my favorites for you kubecon only the best for you i know that there's a lot of passionate emoji enthusiasts showing up to my rust talk you can see a baby yoda a nonsensical upside down alien cowboy a cat that is projecting such panic energy that you can you can feel it and it feels like something that you would feel too and the open source program office train where you can string them together and have the osbo logo just running across the screen that last emoji is the open telemetry logo which is hotel for open telemetry i guess we should talk about open telemetry and tremor what an amazing segue thanks i have a couple of goals for this presentation before we jump in that i want you to know i want you to walk away with knowing what tremor is used for knowing what open telemetry is used for why those two things exist how they came to be and how they can work together so let's just get into it and start with tremor is an early stage event processing system or unstructured data with rich support for structural pattern matching filtering transformation very astute i know uh the best part of being a presenter is reading directly from the slide it's very engaging for your audience i ripped that definition directly from oh it's that way docs.tremor.rs and definitions are fantastic to start with because they show you how many words don't make sense together and i hope that when we come back to it it shows just kind of how much we can really in time that we have together and i think the best way to fit those ideas into people's heads is speaking in a more universal language and speaking in gifs and pic
