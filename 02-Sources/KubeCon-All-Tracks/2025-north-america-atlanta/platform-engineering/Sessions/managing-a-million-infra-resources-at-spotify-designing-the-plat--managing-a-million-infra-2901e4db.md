---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering", "SRE Reliability"]
speakers: ["Oliver Soell", "Fredrik Sommar", "Spotify"]
sched_url: https://kccncna2025.sched.com/event/27FZT/managing-a-million-infra-resources-at-spotify-designing-the-platform-to-manage-change-at-scale-oliver-soell-fredrik-sommar-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Managing+a+Million+Infra+Resources+at+Spotify%3A+Designing+the+Platform+To+Manage+Change+at+Scale+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Managing a Million Infra Resources at Spotify: Designing the Platform To Manage Change at Scale - Oliver Soell & Fredrik Sommar, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Oliver Soell, Fredrik Sommar, Spotify
- Schedule: https://kccncna2025.sched.com/event/27FZT/managing-a-million-infra-resources-at-spotify-designing-the-platform-to-manage-change-at-scale-oliver-soell-fredrik-sommar-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Managing+a+Million+Infra+Resources+at+Spotify%3A+Designing+the+Platform+To+Manage+Change+at+Scale+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Managing a Million Infra Resources at Spotify: Designing the Platform To Manage Change at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZT/managing-a-million-infra-resources-at-spotify-designing-the-platform-to-manage-change-at-scale-oliver-soell-fredrik-sommar-spotify
- YouTube search: https://www.youtube.com/results?search_query=Managing+a+Million+Infra+Resources+at+Spotify%3A+Designing+the+Platform+To+Manage+Change+at+Scale+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Vg2FiJZReDg
- YouTube title: Managing a Million Infra Resources at Spotify: Designing the Platfo... Oliver Soell & Fredrik Sommar
- Match score: 0.825
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/managing-a-million-infra-resources-at-spotify-designing-the-platform-t/Vg2FiJZReDg.txt
- Transcript chars: 30048
- Keywords: platform, spotify, resources, resource, developers, feature, management, developer, google, manage, configuration, regions, question, change, clusters, create, playlist, pretty

### Resumo baseado na transcript

Keep us in mind if you're still looking for a place to listen to music or audiobooks or whatever. Well, there's a team that supports the playlist feature and and that team needs a place to store their playlists. So maybe you could call this the first era of the resource management problem. So in 2020, we started building a platform for resource management based on Kubernetes that we called the declarative infra platform. Uh secondly, we bet on Kubernetes and the Kubernetes resource model or KRM to describe that configuration as Kubernetes objects. The group version kind metadata in the Kubernetes resource model makes this clear.

### Excerpt da transcript

Good morning, KubeCon. >> Good morning. >> I'm guessing most of you have heard of Spotify. Let's see a show of hands. Who's heard of Spotify? >> Oh, that's great. That's great to see. Thank you. Uh, but don't worry, in case you haven't. We're an audio company. Keep us in mind if you're still looking for a place to listen to music or audiobooks or whatever. So, anyway, you're probably familiar with our UI. Here's our app. As you can see, like you got your playlists. Each playlist has a bunch of songs. Well, there's a team that supports the playlist feature and and that team needs a place to store their playlists. This is a pretty common use case at Spotify. And for that type of thing, we use Google Cloud's big table. The playlist team just wants a big table. But there's also a team at Spotify that cares specifically about big tables. They care about the cloud regions they're in, how the autoscaler is configured, whether backups are turned on, and so on. So, how can we make these two teams work together? How do we bridge the feature team that owns their feature in the Spotify app with the platform team that owns an infrastructure domain like storage and big tables?

That's what we're going to talk to talk about today about our resource management platform uh and how it makes that feature developers like the playlist team get the resources they need and that those resources are managed according to the platform developers like the storage big table team uh that care about those resources and then how the platform enables those platform teams to manage those resources at scale. So, hi again. I'm Frederick and hello again. I'm Oliver. And we're both engineers in Spotify's platform organization. And we work closely with our resource management platform where we manage close to a million resources. So, first I'm going to go over a little history to set the stage. Then we're going to look at the current platform in a bit more detail so you can understand how, why, and how we're evolving our platform. So, let's start with a little trip down memory lane. So, we're going to go back not to the beginning of Spotify, but to in 2016 when Spotify moved from data centers into the cloud, Google's cloud platform.

And that story is written in this blog post by our chief architect. Uh here's a QR code if uh it'll take you straight there if you want to read it. But the move to GCP, it was a tremendous success in many ways. But what this blog post doesn't tell you is that we to
