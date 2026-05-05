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
themes: ["Observability"]
speakers: ["Andrea Chomiak", "Dash0"]
sched_url: https://kccncna2025.sched.com/event/27Fbk/designing-for-observability-from-noise-to-insight-andrea-chomiak-dash0
youtube_search_url: https://www.youtube.com/results?search_query=Designing+for+Observability%3A+From+Noise+To+Insight+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Designing for Observability: From Noise To Insight - Andrea Chomiak, Dash0

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Atlanta
- Speakers: Andrea Chomiak, Dash0
- Schedule: https://kccncna2025.sched.com/event/27Fbk/designing-for-observability-from-noise-to-insight-andrea-chomiak-dash0
- Busca YouTube: https://www.youtube.com/results?search_query=Designing+for+Observability%3A+From+Noise+To+Insight+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Designing for Observability: From Noise To Insight.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fbk/designing-for-observability-from-noise-to-insight-andrea-chomiak-dash0
- YouTube search: https://www.youtube.com/results?search_query=Designing+for+Observability%3A+From+Noise+To+Insight+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KGPX3-xasK8
- YouTube title: Designing for Observability: From Noise To Insight - Andrea Chomiak, Dash0
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/designing-for-observability-from-noise-to-insight/KGPX3-xasK8.txt
- Transcript chars: 14252
- Keywords: actually, design, probably, information, understand, default, observability, important, screen, better, systems, always, around, related, process, principle, visual, grouping

### Resumo baseado na transcript

I'm Andrea Homc and this is actually my first CubeCon talk and I know that CubeCom is full of u technical talks and today I want to take all that technicity from a different angle which is uh usability and design because it doesn't matter how technical or advanced our systems are if people can actually use them right. So in this session I want to share with you how good design can help engineers actually turn noisy data into clear insights. And also when these correlated insights meet good design, we finally get clarity. And for that I picked um some of the design principles that I think are the most uh important and also practical so you can start implementing them and understand why they are so uh important to get there. And it's because every good observability tool and actually every good design must have clear information hierarchy because if your users of or if people don't know where to look at they will probably end up not looking at anything at all. And we designers use that to drag your attention to the most important stuff first.

### Excerpt da transcript

Hi, welcome. Um, thank you for being here. I'm Andrea Homc and this is actually my first CubeCon talk and I know that CubeCom is full of u technical talks and today I want to take all that technicity from a different angle which is uh usability and design because it doesn't matter how technical or advanced our systems are if people can actually use them right. So in this session I want to share with you how good design can help engineers actually turn noisy data into clear insights. But first um a quick intro. Uh a designer in this world is not always having fun. So I work at the zero and the zero is an open telemetry native observability tool where my job is to take a really complicated observability data and turn it into something that people can actually use and understand and that that is exactly what I want to share with you today. Um some some of the techniques that I use uh to get there. So let's get started. Uh before I share with you these uh techniques and design principles, I want you to empathize with the pain.

Um so for that, imagine this. Uh it's 2 a.m. and your fast asleep, but you're on call and your phone goes off. So you open the notification and it says uh system degraded. That's it. You are not sure how bad it is, but you got paged. So, you wake up and you get on with it. And there is a link to a dashboard. So, you click on it and you start digging around. You know, a lot of tools, logs, traces, events, and probably too many dashboards. You end up unsure if you need to wake up someone else or just hope for the best. And probably you've been there at least once in your career if you're an engineer. And the interesting bit about these situations is that we tend to blame the tech. So we start asking ourselves like okay maybe it's related to the pipelines or it must be related to infrastructure or the configuration. But what if the real blocker is how the data is presented? Because if during an incident a dashboard makes you more confused, that's probably not a data issue, it's a usability failure. And now um after the pain, uh the good news and is that we're shifting thanks to tools like open telemetry from isolated signals to correlated insights.

And that means probably the end of the eternal tap hopping that we were just mentioning and also the possibility to have the full picture of what's going on with your systems. And also when these correlated insights meet good design, we finally get clarity. And clarity makes our brains happier
