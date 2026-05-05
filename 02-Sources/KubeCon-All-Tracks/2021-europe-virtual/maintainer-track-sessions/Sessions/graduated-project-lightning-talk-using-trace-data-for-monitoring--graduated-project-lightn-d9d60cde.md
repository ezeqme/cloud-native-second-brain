---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Albert Teoh"]
sched_url: https://kccnceu2021.sched.com/event/iaAx/graduated-project-lightning-talk-using-trace-data-for-monitoring-alerting-of-application-health-not-just-debugging-albert-teoh
youtube_search_url: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+Using+Trace+Data+for+Monitoring+%26+Alerting+of+Application+Health%2C+not+Just+Debugging+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Graduated Project Lightning Talk: Using Trace Data for Monitoring & Alerting of Application Health, not Just Debugging - Albert Teoh

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Albert Teoh
- Schedule: https://kccnceu2021.sched.com/event/iaAx/graduated-project-lightning-talk-using-trace-data-for-monitoring-alerting-of-application-health-not-just-debugging-albert-teoh
- Busca YouTube: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+Using+Trace+Data+for+Monitoring+%26+Alerting+of+Application+Health%2C+not+Just+Debugging+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Graduated Project Lightning Talk: Using Trace Data for Monitoring & Alerting of Application Health, not Just Debugging.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iaAx/graduated-project-lightning-talk-using-trace-data-for-monitoring-alerting-of-application-health-not-just-debugging-albert-teoh
- YouTube search: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+Using+Trace+Data+for+Monitoring+%26+Alerting+of+Application+Health%2C+not+Just+Debugging+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EaIqBoiRivs
- YouTube title: Graduated Project Lightning Talk: Using Trace Data for Monitoring & Alerting of Appl... Albert Teoh
- Match score: 0.93
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/graduated-project-lightning-talk-using-trace-data-for-monitoring-alert/EaIqBoiRivs.txt
- Transcript chars: 6912
- Keywords: metrics, processor, application, latency, health, tracing, adding, traces, similar, collector, matrix, documentation, trace, monitoring, little, context, actually, interesting

### Resumo baseado na transcript

hi everyone my name is albert and today i'd like to talk to you about using your trace data for monitoring and alerting of application health and not just for debugging if you're already using a distributed tracing solution like jager hopefully this will give you an appreciation for the additional value that you could gain from your span data without adding more metrics instrumentation and if you're new to distributor tracing hopefully this will give you some motivation to start instrumenting your services and take advantage of the application

### Excerpt da transcript

hi everyone my name is albert and today i'd like to talk to you about using your trace data for monitoring and alerting of application health and not just for debugging if you're already using a distributed tracing solution like jager hopefully this will give you an appreciation for the additional value that you could gain from your span data without adding more metrics instrumentation and if you're new to distributor tracing hopefully this will give you some motivation to start instrumenting your services and take advantage of the application health monitoring you could you could get for free along with the trace data so just a little bit about myself i'm a jager maintainer working at logs io on our distributed tracing product and funnily enough it's based on jager when i do have some spare time i'd like to walk around the garden and just get my hands dirty literally growing vegetables and fruit so traces are a goldmine of of observability data it's rich in context and detail but actually not the majority of those traces are actually not that interesting um once in a while you do find some nuggets of interesting traces like those with errors or slow requests but then the question is what's the best way to find these little nuggets of gold um amongst our our mountain of spans and so to help explain how we do this i want to draw an analogy to how pulsars are detected so parcels are essentially dead stars that are spinning very rapidly emitting radio waves at a clock-like period like much like a lighthouse um so when they're those signals arrive to earth they're mixed in with other noise from either space or earth earth-bound sources like mobile phones or tv or radio radio stations so as you can see from that first row it's not really clear that there is a pulse there amongst all that noise but if we know the period of these pulses then we could cut this signal up into that period and start adding those signals together and so the idea is that the pulse signals would accumulate up while the noise cancels cancels each other out leaving a distinct pulse as we see at the bottom here so the gold and the pulse in our analogy is like the single example error or slow span from a servicer operation and the mountain or soil or the noise it's much like the the millions of spans from hundreds or even thousands of service operations to search through and much like adding the pulsar signal together so that to to find that distinct sig that distinct pulse we aggregate the
