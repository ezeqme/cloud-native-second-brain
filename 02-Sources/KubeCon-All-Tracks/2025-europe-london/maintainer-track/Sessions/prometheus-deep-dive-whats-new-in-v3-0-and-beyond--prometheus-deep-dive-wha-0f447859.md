---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Saswata Mukherjee", "Red Hat", "Fiona Liao", "Grafana Labs"]
sched_url: https://kccnceu2025.sched.com/event/1tcxG/prometheus-deep-dive-whats-new-in-v30-and-beyond-saswata-mukherjee-red-hat-fiona-liao-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+Deep+Dive%3A+What%E2%80%99s+New+in+v3.0+and+Beyond+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Prometheus Deep Dive: What’s New in v3.0 and Beyond - Saswata Mukherjee, Red Hat & Fiona Liao, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Saswata Mukherjee, Red Hat, Fiona Liao, Grafana Labs
- Schedule: https://kccnceu2025.sched.com/event/1tcxG/prometheus-deep-dive-whats-new-in-v30-and-beyond-saswata-mukherjee-red-hat-fiona-liao-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Prometheus+Deep+Dive%3A+What%E2%80%99s+New+in+v3.0+and+Beyond+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Prometheus Deep Dive: What’s New in v3.0 and Beyond.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcxG/prometheus-deep-dive-whats-new-in-v30-and-beyond-saswata-mukherjee-red-hat-fiona-liao-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Prometheus+Deep+Dive%3A+What%E2%80%99s+New+in+v3.0+and+Beyond+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KS_rGWazTio
- YouTube title: Prometheus Deep Dive: What’s New in v3.0 and Beyond - Saswata Mukherjee & Fiona Liao
- Match score: 0.852
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/prometheus-deep-dive-whats-new-in-v3-0-and-beyond/KS_rGWazTio.txt
- Transcript chars: 24098
- Keywords: prometheus, native, histograms, remote, write, metrics, support, changes, metric, format, bucket, metadata, everyone, labels, classic, histogram, querying, directly

### Resumo baseado na transcript

Hopefully you managed to catch some good talks already and are just not too sleepy after lunch. Um, so in this talk we will be going to take you taking you through Prometheus V3, what's new in that and talk a bit about the future work beyond V3. Um so for Prometheus deep dive talks um we like to do this fun exercise um before we start. Now, uh, put or keep your hand up if you know what the plural of Prometheus is. Um, so it's a metricbased monitoring and alerting toolkit created at SoundCloud in 2012 and it joined the CNCF in 2016 as the second project to do so after um, Kubernetes. Um what Prometheus offers is a rich instrumentation ecosystem, data collection and storage and querying alerting and visualization support.

### Excerpt da transcript

Hey everyone. Uh, glad to see you all here at CubeCon London today. Hopefully you managed to catch some good talks already and are just not too sleepy after lunch. Um, so in this talk we will be going to take you taking you through Prometheus V3, what's new in that and talk a bit about the future work beyond V3. Cool. So uh, hi everyone. I'm Fiona. I'm a software engineer at Grafana Labs and uh I mostly work on Prometheus and Grafana Mimir there. Um in Prometheus I've worked on stuff like out of order native histograms as well as helping to coordinate the V3 release and I've recently become a Prometheus team member. So uh yay for me I guess. Um this picture is from the last time I was here at the Excel Center. So that was a couple years ago and I was doing a sports event and my watch picked up that I may have been a little stressed. So I'm hoping this talk will be uh less nerve-wracking than that. Yeah. And my name is Saswata Mukharji. I'm a senior software engineer at Red Hat where I work on monitoring platforms largely based around Tanus and Prometheus.

I'm a maintainer of Tanas as well and a newly minted Prometheus team member. I also help maintain certain other um CNCF adjacent go tools and libraries. And you can find me as the chasm code pretty much anywhere. Um so yeah um a little bit of audience participation to start which we all know and love. Um so for Prometheus deep dive talks um we like to do this fun exercise um before we start. So um first uh raise your hands if you know what Prometheus is. Oh very nice. Cool. Uh keep your hand up if you use Prometheus. Okay. And now keep your hand up if you use Prometheus at scale. Awesome. Um, one last question then. Now, uh, put or keep your hand up if you know what the plural of Prometheus is. Awesome. Okay, cool. Some real experts here, I see. Um, but yeah, if you didn't know, it's uh, Promethei, and there's a fun talk on why. Um, but yeah, now we know the plural is Prometheus. Uh, what even is it? Just as a bit of a recap. Um, so it's a metricbased monitoring and alerting toolkit created at SoundCloud in 2012 and it joined the CNCF in 2016 as the second project to do so after um, Kubernetes.

If you're curious about the backstory, um, there's a nice documentary on it on YouTube which goes through its inception and its journey to becoming the widely used open source project it is today. Um what Prometheus offers is a rich instrumentation ecosystem, data collection and storage and querying alerting and
