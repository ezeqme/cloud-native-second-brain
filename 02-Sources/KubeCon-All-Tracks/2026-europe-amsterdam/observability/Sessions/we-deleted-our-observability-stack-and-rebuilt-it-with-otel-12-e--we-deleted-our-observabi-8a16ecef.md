---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Observability"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Yash Sharma", "Kunju Perath", "DigitalOcean"]
sched_url: https://kccnceu2026.sched.com/event/2CVxh/we-deleted-our-observability-stack-and-rebuilt-it-with-otel-12-engineers-to-4-at-20k+-clusters-yash-sharma-kunju-perath-digitalocean
youtube_search_url: https://www.youtube.com/results?search_query=We+Deleted+Our+Observability+Stack+and+Rebuilt+It+With+OTEL%3A+12+Engineers+to+4+at+20K%2B+Clusters+CNCF+KubeCon+2026
slides: []
status: parsed
---

# We Deleted Our Observability Stack and Rebuilt It With OTEL: 12 Engineers to 4 at 20K+ Clusters - Yash Sharma & Kunju Perath, DigitalOcean

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yash Sharma, Kunju Perath, DigitalOcean
- Schedule: https://kccnceu2026.sched.com/event/2CVxh/we-deleted-our-observability-stack-and-rebuilt-it-with-otel-12-engineers-to-4-at-20k+-clusters-yash-sharma-kunju-perath-digitalocean
- Busca YouTube: https://www.youtube.com/results?search_query=We+Deleted+Our+Observability+Stack+and+Rebuilt+It+With+OTEL%3A+12+Engineers+to+4+at+20K%2B+Clusters+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre We Deleted Our Observability Stack and Rebuilt It With OTEL: 12 Engineers to 4 at 20K+ Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVxh/we-deleted-our-observability-stack-and-rebuilt-it-with-otel-12-engineers-to-4-at-20k+-clusters-yash-sharma-kunju-perath-digitalocean
- YouTube search: https://www.youtube.com/results?search_query=We+Deleted+Our+Observability+Stack+and+Rebuilt+It+With+OTEL%3A+12+Engineers+to+4+at+20K%2B+Clusters+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Z0oum6Eh1is
- YouTube title: We Deleted Our Observability Stack and Rebuilt It With OTEL: 12 Engine... Yash Sharma & Kunju Perath
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/we-deleted-our-observability-stack-and-rebuilt-it-with-otel-12-enginee/Z0oum6Eh1is.txt
- Transcript chars: 31298
- Keywords: basically, cluster, control, digitalocean, prometheus, observability, actually, customer, managed, logs, attributes, wanted, resource, worker, metrics, earlier, called, literally

### Resumo baseado na transcript

And today we'll be covering about the observability part that we do at DigitalOcean uh for our managed community service. So, before going ahead and we start the session, I would like to give a quick introduction about me and my co-speaker. So, now you have got the idea of at what a scale in today's session we'll be talking about and why actually it matters and it becomes really difficult when you're talking about the observability of 20,000 clusters. We have like uh we have good observability on our control plane and uh we have the control plane longs uh long-term storage as well. So, if I give you an idea on what what not what was not working, so we were not able we don't used to have very good communities audit logs. What happened like 5 days ago?" Uh sometimes we were not able to answer that question because we used to have a file-based uh storage and we used to lose them uh when communities cluster restarts.

### Excerpt da transcript

So, let's kick kick off our today's session. And today we'll be covering about the observability part that we do at DigitalOcean uh for our managed community service. So, before going ahead and we start the session, I would like to give a quick introduction about me and my co-speaker. So, I'm Yash. I work at DigitalOcean as a developer advocate and I'm also a maintainer of CNCF projects as well. So, I've been very very uh contributing in CNCF for a while as well. With me uh I have a great uh engineer as well, Kunju, uh from the DigitalOcean managed communities team itself as well. So, what we will be covering today, we will be covering like what actually DigitalOcean managed communities service is and why observability and uh the title like why we went with the hotel and everything and uh our telemetry part. We will go through the architecture as well, which will be more like a case study. And uh we'll be talking about the hotel and at last you will see what are the lessons we have learned throughout those years while working at such large scale.

Moving forward, I would like to give you a quick idea of uh at what a scale we are going to talk about at today's talk. So, to give an idea, the DOKS team is of 18 people right now, which manages more than 20,000 plus clusters running inside DigitalOcean across the 13 cloud regions. We are upstream certified with the CNCF and uh certified host for the communities as a management platform as well. Uh we power open source. We love open source as a DigitalOcean. I'm not sure how many of you know the Hacktoberfest, but we love open source. So, we are powered by open source as well. And uh we are achieving 99.97 uptime for our DOKS platform. Uh at DigitalOcean we uh promise for 99.95, but last year we managed 99.97, which was really really great. And uh dog food side is like we build on our own products. So, if you know the droplet, it's like an instance uh for DigitalOcean and we use our own products to build the products. That's it. So, now you have got the idea of at what a scale in today's session we'll be talking about and why actually it matters and it becomes really difficult when you're talking about the observability of 20,000 clusters.

So, just to give an idea why observability for us, it's like detect issues before it gets to actual customers, right? You want to make sure that we are able to detect the issues before even customer coming us to us and complaining about it, right? So, that's why observability
