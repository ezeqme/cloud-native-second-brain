---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Stefan Särne", "Spotify"]
sched_url: https://kccnceu2025.sched.com/event/1txAH/set-your-developers-free-fleet-management-at-spotify-stefan-sarne-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Set+Your+Developers+Free%3A+Fleet+Management+at+Spotify+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Set Your Developers Free: Fleet Management at Spotify - Stefan Särne, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: Stefan Särne, Spotify
- Schedule: https://kccnceu2025.sched.com/event/1txAH/set-your-developers-free-fleet-management-at-spotify-stefan-sarne-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Set+Your+Developers+Free%3A+Fleet+Management+at+Spotify+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Set Your Developers Free: Fleet Management at Spotify.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txAH/set-your-developers-free-fleet-management-at-spotify-stefan-sarne-spotify
- YouTube search: https://www.youtube.com/results?search_query=Set+Your+Developers+Free%3A+Fleet+Management+at+Spotify+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Zr7y27HpII4
- YouTube title: Set Your Developers Free: Fleet Management at Spotify - Stefan Särne, Spotify
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/set-your-developers-free-fleet-management-at-spotify/Zr7y27HpII4.txt
- Transcript chars: 24021
- Keywords: change, actually, management, changes, anyway, pretty, everybody, couple, course, incident, automation, update, software, review, making, components, component, spotify

### Resumo baseado na transcript

Not that you have it next to your bed, but anyway, let's pick it up there. Uh but of course somebody was woken up by this security incident and I don't know because I didn't see it but I can imagine the face was basically like this. Also understand the scope of the problem because again this was for our backend services and we have we have more than two. We set up a meeting that they can jump in and understand the problem, the questions, whatever they have. But anyway, you do that, you get to a place, I'm sure you also start assessing what was the how much of the problem was there any was there any actual security breach in this case or or did we manage etc. another number of this uh the number of lines of code each engineering Spotify owns has doubled in the last two years so that's a problem so what do you do with such a problem well you invest in taking care of it Another way

### Excerpt da transcript

Hello everybody. Let's see if we can get some. Yeah, we have it on st screen as well. So I wanted to try out with a little bit of storytelling here. So imagine waking up, picking up your phone. Not that you have it next to your bed, but anyway, let's pick it up there. And this is the first feed you read. Happen to work at Spotify as well. This is pretty scary actually. So we have something that can execute code in our back end. All our backend services. Yes, they are Java services. That's a pretty that's a pretty daunting way to wake up. is not true because this blog coming up a couple of days later. Uh but of course somebody was woken up by this security incident and I don't know because I didn't see it but I can imagine the face was basically like this. This is going to be a long day. Uh so yeah that was a problem a couple of years ago. We know it as the log forj incident. It's important to us in Spotify because it was a pivotal moment on how we operate our fleet. My name is Stefan. I want to share a little bit on how we were at the storytelling style.

Not ever going to be 100% true but anyway how we were working such an incident how we could have been working it earlier because again this is why we are working on fleet management how we take the pain away from most of our engineers. So yeah how would you do that? How what would happen you wake up you try to understand a problem right first question is this a problem? Yeah, it's bad. Somebody can execute whatever they code they like in your back end. That's bad. It's okay. It's a problem. It's a problem. Is it a problem for us though? No, we're fine, right? Because we're using another logging system. So, we're actually It's all good. It's all good. Aside from the fact that we're also using libraries which are using log forj. So, yeah, maybe not that fine anyway. Uh, and also we have many disciplines. Another one is the data discipline and we have a we have a data processing framework called Shio which is also running on the JVM. It's in Scola but the library is log forj is in Java. So yeah yeah this is kind of a problem.

Okay cool. So the next thing is of course to really read the incident understand the fix apply it. It was pretty easy in this case. There is a next version. This next version has solved the problem. just update the version of it, test it, deploy it, there you're done. Also understand the scope of the problem because again this was for our backend services and we have we have more than
