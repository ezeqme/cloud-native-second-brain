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
themes: ["AI ML", "Community Governance"]
speakers: ["Leonardo Alminana", "Chronosphere"]
sched_url: https://kccnceu2025.sched.com/event/1ue2s/fluent-bit-v4-a-decade-of-innovation-and-whats-next-leonardo-alminana-chronosphere
youtube_search_url: https://www.youtube.com/results?search_query=Fluent+Bit+v4%3A+A+Decade+of+Innovation+and+What%E2%80%99s+Next+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Fluent Bit v4: A Decade of Innovation and What’s Next - Leonardo Alminana, Chronosphere

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Leonardo Alminana, Chronosphere
- Schedule: https://kccnceu2025.sched.com/event/1ue2s/fluent-bit-v4-a-decade-of-innovation-and-whats-next-leonardo-alminana-chronosphere
- Busca YouTube: https://www.youtube.com/results?search_query=Fluent+Bit+v4%3A+A+Decade+of+Innovation+and+What%E2%80%99s+Next+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Fluent Bit v4: A Decade of Innovation and What’s Next.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1ue2s/fluent-bit-v4-a-decade-of-innovation-and-whats-next-leonardo-alminana-chronosphere
- YouTube search: https://www.youtube.com/results?search_query=Fluent+Bit+v4%3A+A+Decade+of+Innovation+and+What%E2%80%99s+Next+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ae2-LNHtUr8
- YouTube title: Fluent Bit v4: A Decade of Innovation and What’s Next - Leonardo Alminana, Chronosphere
- Match score: 0.847
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/fluent-bit-v4-a-decade-of-innovation-and-whats-next/Ae2-LNHtUr8.txt
- Transcript chars: 22773
- Keywords: fluent, logs, traces, metrics, processor, plugins, information, processing, sampling, write, trace, plug-in, picture, actually, important, trying, integrations, interesting

### Resumo baseado na transcript

So for those who had to wait, I hope you took uh the opportunity to take a picture of the of the webinar that Eduardo, the project leader, is going to be giving in about 20 days. That one's going to be pretty good and it's going to be a bit more extensive than this one. Uh a mere 10 years ago, we were basically just moving logs around and nowadays we are doing everything from logs to traces to profiles. I think that we all uh can see how the like the picture that we get in the in our heads like the joke about the um spherical co uh cow in the vacuum chamber chamber you know we think about logs we think about metrics and traces maybe and we have this picture where we are going to analyze the data we are going to extract value from it and we are going to be happy. But the problem is that things are usually very chaotic and they are growing even more chaotic each day.

### Excerpt da transcript

Thanks for coming to this presentation. Uh I'm a bit of a stickler when it comes to starting on time. So for those who had to wait, I hope you took uh the opportunity to take a picture of the of the webinar that Eduardo, the project leader, is going to be giving in about 20 days. That one's going to be pretty good and it's going to be a bit more extensive than this one. So this presentation is going to talk about the the history like where we come from, where we are right now and where we're going. The idea is to to give a a good complete picture for those of you who are not um aware of what flame bit is or where we are and uh for those who who are and are looking forward to version 4.0 zero we which we released on Monday. Uh I'm going to talk a little bit about the new features uh we have just introduced and the the ones that we would like to introduce in the new fe in the near future and the long term. As you probably know the telemetry arena has been uh evolving through the past 10 years. Well, probably more, but but the the trend is that things are growing exponentially.

We're generating more and more data uh and more and more types of data. Uh a mere 10 years ago, we were basically just moving logs around and nowadays we are doing everything from logs to traces to profiles. So things are only going to grow and get even more hectic, which means that we need to be extra um on top of things to be able to exploit that data and not just spend money storing stuff that we don't care. I think that we all uh can see how the like the picture that we get in the in our heads like the joke about the um spherical co uh cow in the vacuum chamber chamber you know we think about logs we think about metrics and traces maybe and we have this picture where we are going to analyze the data we are going to extract value from it and we are going to be happy. However, reality is not a vacuum chamber. I guess um I guess that's good. But the problem is that things are usually very chaotic and they are growing even more chaotic each day. So we get the logs, we got the metrics, we get the traces, everyone has a different standard.

Some of them have their own standards, some of them come from like the olden days. And uh we need to make sense of that to be able to extract value. Otherwise, it's it just doesn't make any any any any reason. And I think I'm not the only one who probably feels overwhelmed when it's when one faces this situation. It's like what am I supposed to do wi
