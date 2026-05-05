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
themes: ["Observability", "Runtime Containers", "Kubernetes Core"]
speakers: ["Simon Schrottner", "Dynatrace", "Manuel Timelthaler", "Tractive"]
sched_url: https://kccnceu2026.sched.com/event/2CW7W/18-bluetooth-controllers-walk-into-a-bar-observability-runtime-configuration-with-cncf-tools-simon-schrottner-dynatrace-manuel-timelthaler-tractive
youtube_search_url: https://www.youtube.com/results?search_query=18+Bluetooth+Controllers+Walk+into+a+Bar%3A+Observability+%26+Runtime+Configuration+with+CNCF+Tools+CNCF+KubeCon+2026
slides: []
status: parsed
---

# 18 Bluetooth Controllers Walk into a Bar: Observability & Runtime Configuration with CNCF Tools - Simon Schrottner, Dynatrace & Manuel Timelthaler, Tractive

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Simon Schrottner, Dynatrace, Manuel Timelthaler, Tractive
- Schedule: https://kccnceu2026.sched.com/event/2CW7W/18-bluetooth-controllers-walk-into-a-bar-observability-runtime-configuration-with-cncf-tools-simon-schrottner-dynatrace-manuel-timelthaler-tractive
- Busca YouTube: https://www.youtube.com/results?search_query=18+Bluetooth+Controllers+Walk+into+a+Bar%3A+Observability+%26+Runtime+Configuration+with+CNCF+Tools+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre 18 Bluetooth Controllers Walk into a Bar: Observability & Runtime Configuration with CNCF Tools.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW7W/18-bluetooth-controllers-walk-into-a-bar-observability-runtime-configuration-with-cncf-tools-simon-schrottner-dynatrace-manuel-timelthaler-tractive
- YouTube search: https://www.youtube.com/results?search_query=18+Bluetooth+Controllers+Walk+into+a+Bar%3A+Observability+%26+Runtime+Configuration+with+CNCF+Tools+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Y9agHID8Ml4
- YouTube title: 18 Bluetooth Controllers Walk into a Bar: Observability & R... Simon Schrottner & Manuel Timelthaler
- Match score: 0.776
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/18-bluetooth-controllers-walk-into-a-bar-observability-runtime-configu/Y9agHID8Ml4.txt
- Transcript chars: 18449
- Keywords: little, controllers, observability, actually, acceleration, thought, player, metrics, bluetooth, basically, happening, running, already, raspberry, everything, prometheus, couple, course

### Resumo baseado na transcript

We're super glad that so many people showed up to the last talk of this year's CubeCon. We'll be talking about observability and runtime configuration with CNCF tools for a party game, for a real-time party game. So we thought we we overengineered a lot of stuff and thought well having the observability stack on the same machine that would definitely not work and it would definitely problem. So we had the possibility to actually combine everything into this nice little overengineered architecture on one small little device. Of course we also want metrics and for that first you have to understand all the game input is basically from the motion sensor. And we were using Prometheus for getting yeah the matrix data uh somewhere and Prometheus primarily is a pool based system or the majority of people use it with scraping and the default is 60 seconds.

### Excerpt da transcript

Hello everyone. Hello. We're super glad that so many people showed up to the last talk of this year's CubeCon. Thank you for being here. Thank you. We're honored. We try to make this entertaining for you so you won't regret it. 18 Bluetooth controllers walk into a bar. We'll be talking about observability and runtime configuration with CNCF tools for a party game, for a real-time party game. And for that, of course, you first have to understand what is this game we're talking about. Yeah. And that actually brings us to those PlayStation Move controllers. Actually, you can imagine this is an acceleration based game where it's uh where those controllers are like a spoon with egg on it and you try to protect your egg while you while you try to make the other lose their egg. Just to give you a little fun demo. Let's see who wins. Basically, when the game is starting, it's like this. And then you try to to to Yeah, perfect. You try to push the other around. And that's the whole sense of the game. And we try to So, and this game is really fun.

It's a really nice icebreaker. I love to bring this to conferences because, as I said, you uh you're finding people, you talk a little bit is a really good starting point. But from now and then when I brought this game to conferences, there was always this this moment when suddenly something was not happening. It's an open source game running on a rasper without any kind of monitor and it was really really frustrating. >> But Simon, don't you work at an observability company? >> Yes, I'm working actually at an observability company and I should know how this is how how I could get more insights into that. I'm working at Dino but in the end the thing was well for me this does not look like my usual cloudnative workflows. this looks for me like a little bit of IoT and I thought well I know somebody who works at an IoT company and that's why I asked Manu if you can help me with that. Hi I'm work attractive. We're one of the global leaders in health and location tracking for pets and while we as a company do work with hardware a lot I don't.

I work on the web services but hey sounds interesting I mean so we asked ourselves basically the question how can we make this little tool a little how can we know what's going on how can we get a little bit of observability into it I mean we already have in the CNCF this really cool technologies like open telemetry and as I'm an open feature maintainer I thought well let's sprinkle a li
