---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Eduardo Silva", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFz6/project-lightning-talk-fluent-bit-v5-eduardo-silva-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Fluent+Bit+V5+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Fluent Bit V5 - Eduardo Silva, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Eduardo Silva, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFz6/project-lightning-talk-fluent-bit-v5-eduardo-silva-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Fluent+Bit+V5+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Fluent Bit V5.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFz6/project-lightning-talk-fluent-bit-v5-eduardo-silva-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Fluent+Bit+V5+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BwpXIkXOLOU
- YouTube title: Project Lightning Talk: Fluent Bit V5 - Eduardo Silva, Maintainer
- Match score: 0.822
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-fluent-bit-v5/BwpXIkXOLOU.txt
- Transcript chars: 5354
- Keywords: fluent, version, better, analysis, collect, security, processor, receive, performance, support, matrix, pipeline, general, implemented, collector, process, observability, nobody

### Resumo baseado na transcript

And nobody wakes up a morning saying I want to do telemetry observability. But in order to accomplish data analysis, you want to move the data that are in your host in your logs from your application or matrix or traces and send that to a place where you can analyze it. We're going to talk about open telemetry, data processing, platform security, and performance in general. So having a lower CPU and lower memory overhead is a must for us plus security. So if you like to collect metrics and you want to reduce and just collect the delta between your sample of counters, yeah, you can use this with your new processor available. And we rearchitect internally how our HTTP server receive connections connections and can scale up to process the data in all it layers.

### Excerpt da transcript

How are you guys? All good. I know we are after lunch. We need to get this energy up. So I will try to this as much informative as possible. My name is Eduardo Silva. You might be familiar with Fluent Bit project or Fluentd. Please raise your hand pretty quickly. If not, I will do a better job explaining what do we solve. And here we go. So telemetry data or inside observability exist in many forms. And nobody wakes up a morning saying I want to do telemetry observability. Nobody. Right? Because what you want to accomplish is data analysis. Right? But in order to accomplish data analysis, you want to move the data that are in your host in your logs from your application or matrix or traces and send that to a place where you can analyze it. And that's what fluent bit. Fluent bit is a telemetry pipeline that allows you to collect all this information through different components that are called inputs. So how do we collect data from multiple sources? We have the concept of processors where you take this data sometimes you remove duplicates or offuscate for security and then you allow to route this data to the right backends for analysis and I say backends because some people might leverage Splunk others might use Google stack drive or elastic search and so on.

So fluent bit as an agent as an architecture that is based on plugins and these plugins I need to implement these different components that we were talking about in the pipeline. So we have for inputs for processor for outputs we have for example Lua for the scripting we can fetch Kubernetes metadata and so on and where fluent bit runs it runs on IoT devices who run Linux any type of node BM bare metal machines or you can deploy it as a gateway to receive data and aggregate them and the principles of this project that has been running for 10 years is like it beat high performance with low resource usage the gold if If you're going to run your your car really really fast, you want you don't want to waste all your gas. That's what Fluent Bit does and it's fully vendor neutral and it has a whole broad ecosystem support. And today we're going to introduce what we are shipping with Fluent Bit V5 that is being released today. Hopefully CI passes. No, it's all good. So good. So the first one is all um um well let me give you a brief.

We're going to talk about open telemetry, data processing, platform security, and performance in general. So from interoperability for open telemetry, we just updated to suppor
