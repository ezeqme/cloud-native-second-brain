---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Ben Kochie", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcw3/project-lightning-talk-prometheus-30-speedrun-ben-kochie-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Prometheus+3.0+Speedrun+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Prometheus 3.0 Speedrun - Ben Kochie, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Ben Kochie, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcw3/project-lightning-talk-prometheus-30-speedrun-ben-kochie-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Prometheus+3.0+Speedrun+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Prometheus 3.0 Speedrun.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcw3/project-lightning-talk-prometheus-30-speedrun-ben-kochie-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Prometheus+3.0+Speedrun+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NRL-bSYVi7Q
- YouTube title: Project Lightning Talk: Prometheus 3.0 Speedrun - Ben Kochie, Maintainer
- Match score: 0.887
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-prometheus-3-0-speedrun/NRL-bSYVi7Q.txt
- Transcript chars: 4038
- Keywords: prometheus, native, almost, hundreds, additional, histograms, coming, speedrun, welcome, feature, features, breaking, changes, version, commits, million, series, sharding

### Resumo baseado na transcript

Uh there are so many different things, it's hard to go through this in 5 minutes, but what I've got now is uh a quick summary. So things that were feature flags in Prometheus 2.0 are now on by default uh and available for use. Uh in Prometheus 2.0 we rewrote the TSDB and it took uh some time to really stabilize and improve the performance and efficiency. Uh and if you really want to know more about Prometheus 3.0 there's going to be a deep dive talk uh on Wednesday. Okay, so one of the other fun things with Prometheus 3.0 is we're almost we were trying to declare it stable, but we're almost there. In Prometheus, we are also working on uh native histogram custom B boundaries u which means you'll be uh Prometheus will be able to read classic Prometheus histograms and convert them into native histograms uh on the fly and it significantly reduces the storage costs

### Excerpt da transcript

Hello, my name is Ben Koshi. I'm on the Prometheus team. Welcome to the Prometheus 3.0 speedrun. So, Prometheus 3.0, we released it last November. It's been really awesome. Uh there are so many different things, it's hard to go through this in 5 minutes, but what I've got now is uh a quick summary. So, uh the big fun, we built a new UI. It's really pretty. It has a bunch of nice things to help you learn how to use PromQL. um we mostly were uh enabling and removing a bunch of feature flags. So things that were feature flags in Prometheus 2.0 are now on by default uh and available for use. Lots of nice graduated features um uh and the migration is super easy. There's not actually uh a lot of breaking changes that we had to include in Prometheus 3.0, but there are a few small things. So we bumped major version. Um 7 years of stability is just insane for an open source project in the cloudnative space. Uh there uh Prometheus 2.0 was fully upgradeable all the way through 3.0 with no breaking changes. Um there are almost 10,000 commits between 2.0 and 3.0 and we've already reached a thousand commits in 3.0.

um hundreds and hundreds of contributors to the just Prometheus itself, not including the additional hundreds that are part of the original, uh uh the additional features in our community. Um uh I used to say a long time ago that in Prometheus 2.0, well, you know, if you get to about a million series, you might want to start thinking about sharding. Now today, I don't even start tell people to worry about sharding until you reach 10 million active series. uh the most of that has come from the efficiency gains. Uh in Prometheus 2.0 we rewrote the TSDB and it took uh some time to really stabilize and improve the performance and efficiency. And so Prometheus today is not the Prometheus it was 7 years ago. Uh and if you really want to know more about Prometheus 3.0 there's going to be a deep dive talk uh on Wednesday. Uh go check it out. I'll pause here for another few more seconds if you want to scan this QR code. Three, two, one, go. Okay, so one of the other fun things with Prometheus 3.0 is we're almost we were trying to declare it stable, but we're almost there.

We're going to have native histograms. Uh this is a really really amazing amount of additional power for histogram data types. In Prometheus, we are also working on uh native histogram custom B boundaries u which means you'll be uh Prometheus will be able to read classic Prometheus histograms and c
