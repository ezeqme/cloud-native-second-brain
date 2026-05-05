---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Experience"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Jaden Walderich", "Alex Mizerak", "Ziax Ltd."]
sched_url: https://kccnceu2026.sched.com/event/2CW3P/from-creepers-to-clusters-evolving-minecraft-into-a-cloud-native-platform-jaden-walderich-alex-mizerak-ziax-ltd
youtube_search_url: https://www.youtube.com/results?search_query=From+Creepers+to+Clusters%3A+Evolving+Minecraft+Into+a+Cloud+Native+Platform+CNCF+KubeCon+2026
slides: []
status: parsed
---

# From Creepers to Clusters: Evolving Minecraft Into a Cloud Native Platform - Jaden Walderich & Alex Mizerak, Ziax Ltd.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jaden Walderich, Alex Mizerak, Ziax Ltd.
- Schedule: https://kccnceu2026.sched.com/event/2CW3P/from-creepers-to-clusters-evolving-minecraft-into-a-cloud-native-platform-jaden-walderich-alex-mizerak-ziax-ltd
- Busca YouTube: https://www.youtube.com/results?search_query=From+Creepers+to+Clusters%3A+Evolving+Minecraft+Into+a+Cloud+Native+Platform+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre From Creepers to Clusters: Evolving Minecraft Into a Cloud Native Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW3P/from-creepers-to-clusters-evolving-minecraft-into-a-cloud-native-platform-jaden-walderich-alex-mizerak-ziax-ltd
- YouTube search: https://www.youtube.com/results?search_query=From+Creepers+to+Clusters%3A+Evolving+Minecraft+Into+a+Cloud+Native+Platform+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XAJySxpKdzo
- YouTube title: From Creepers to Clusters: Evolving Minecraft Into a Cloud Native... Jaden Walderich & Alex Mizerak
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/from-creepers-to-clusters-evolving-minecraft-into-a-cloud-native-platf/XAJySxpKdzo.txt
- Transcript chars: 25471
- Keywords: platform, server, minecraft, servers, started, wanted, basically, players, cubecraft, course, around, trying, running, actually, decided, effectively, player, addition

### Resumo baseado na transcript

Um, our talk is basically a journey of one of the biggest Minecraft servers. probably around 50% of you have at some point tried to play the multiplayer version of Minecraft. And it's never a bad problem to have too many players, but you never want to fail from your own success. And so as we started hitting those numbers and as we started seeing all these players joining CubeCraft, it was very clear to us that we needed to scale. We wanted to support more players dynamically and we wanted to scale and eliminate these single points of failures. We wanted an actual server orchestrator that could dynamically scale and we needed to eliminate that single point of failure.

### Excerpt da transcript

All right. Hello everyone. Um, welcome to our talk. My name is Alex and I'm here together with my colleague Jaden. Um, we are both platform engineers at a company called ZAX. Um, our talk is basically a journey of one of the biggest Minecraft servers. Um, so you've all probably heard about a game called Minecraft. Some of you have probably played it. Some of you um maybe seen the movie. probably around 50% of you have at some point tried to play the multiplayer version of Minecraft. Um, and maybe around 20% of you have tried to run their own Minecraft server. But have you ever wondered what happens if there's suddenly thousands of players trying to join your Minecraft server? Well, that's what this talk is about. So, it all started in 2012 when Keepcraft was established. Originally, it was supposed to be just a small Minecraft server, a safe space for a few friends to play together. But it quickly became popular, and that's where it all started. So, between years 2013 and 14, the server started getting more and more popular.

Within just three years, we've managed to hit around 30,000 concurrent players, and we were not expecting this. Um so it is important to mention that at that time we've all been just teenagers we didn't have any degree in a computer science or we didn't have any formal experience and so our infrastructure looked something like this. Um so since we weren't having any jobs we were just teenagers we also didn't have a budget to buy a fancy powerful servers so we had to work around it. Um, we were overcooking overclocking our servers to make sure we can allow more players to join the game. Um, and when you look inside what the ser inside the servers, this is how it looked like. Um, each server was running a single instance of a Minecraft server that was basically the the copy of the game that allows the players to join the server and play um on our world. In addition to that, we had a separate instance which was also running a Minecraft server, but there were no players. That was our backend solution.

So, we just had a Minecraft server with a different code, different plug-in that was basically communicating with all the other servers through IRC um to make sure players can play the game they want. Um, so we use no frameworks, no orchestration, no containers, nothing at all. Just the IRC network, um, and few micro servers and that's basically it. Thank you, Alex. So, one of the things we found is that we were having explosive growth with
