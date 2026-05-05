---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Nick Rutigliano", "Daniel de Repentigny", "Spotify"]
sched_url: https://kccnceu2024.sched.com/event/1YeO2/how-spotify-re-created-our-entire-backend-without-skipping-a-beat-nick-rutigliano-daniel-de-repentigny-spotify
youtube_search_url: https://www.youtube.com/results?search_query=How+Spotify+Re-Created+Our+Entire+Backend+Without+Skipping+a+Beat+CNCF+KubeCon+2024
slides: []
status: parsed
---

# How Spotify Re-Created Our Entire Backend Without Skipping a Beat - Nick Rutigliano & Daniel de Repentigny, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: France / Paris
- Speakers: Nick Rutigliano, Daniel de Repentigny, Spotify
- Schedule: https://kccnceu2024.sched.com/event/1YeO2/how-spotify-re-created-our-entire-backend-without-skipping-a-beat-nick-rutigliano-daniel-de-repentigny-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=How+Spotify+Re-Created+Our+Entire+Backend+Without+Skipping+a+Beat+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre How Spotify Re-Created Our Entire Backend Without Skipping a Beat.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeO2/how-spotify-re-created-our-entire-backend-without-skipping-a-beat-nick-rutigliano-daniel-de-repentigny-spotify
- YouTube search: https://www.youtube.com/results?search_query=How+Spotify+Re-Created+Our+Entire+Backend+Without+Skipping+a+Beat+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Iw5Tox2H87A
- YouTube title: How Spotify Re-Created Our Entire Backend Without Skipping a Beat
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/how-spotify-re-created-our-entire-backend-without-skipping-a-beat/Iw5Tox2H87A.txt
- Transcript chars: 39987
- Keywords: clusters, cluster, actually, workloads, support, platform, question, product, golden, across, spotify, workload, within, traffic, running, thanks, course, themselves

### Resumo baseado na transcript

all right hey everyone uh Welcome to our talk we'll get into it here so um yeah we're from uh we're spot from Spotify we're going to be talking about how we recreated our entire backend without skipping a beat um so my name is Dan I'm a PM I work on our compute platform and our uh in our Compu networking product area and I'm Nick I'm an SRE working on our compute platform and our networking infrastructure so if you don't know Spotify um yeah it's that one

### Excerpt da transcript

all right hey everyone uh Welcome to our talk we'll get into it here so um yeah we're from uh we're spot from Spotify we're going to be talking about how we recreated our entire backend without skipping a beat um so my name is Dan I'm a PM I work on our compute platform and our uh in our Compu networking product area and I'm Nick I'm an SRE working on our compute platform and our networking infrastructure so if you don't know Spotify um yeah it's that one uh we do music things um and um and yeah we uh we work on the uh the platform there so um one of our core values is uh playfulness um and sometimes what that means is you get team names that don't really mean much so we work on a team called Alf um which is yes from the show from the late 80s um and um you might be thinking what's the best place to get support for a team that's called Alf and that would be of course at mail um so that's super confusing for our users but um that's kind of how we do things um so in terms of scale um these numbers are actually we got them approved so that we could share them with you we haven't talked about these publicly before uh while the stuff on the left is all public but all the things on the right um that's all brand new stuff so yeah in terms of scale um about 62 million uh monthly active users um in about 180 markets um from the platform side of things we're about uh 2800 Engineers over 500 squads that's another thing we call them squads as opposed to teams we do about 2900 production deployments a day over 3,200 microservices and then in terms of like compute itself um were over 40,000 VMS these are all at Peak numbers over across about a million cores 4 pedabytes of memory about a half a million kubernetes pods um and then yeah the big one there 1.5 terabytes per second of egress which is actually larger than the U Amsterdam internet exchange so yeah we uh we have quite a bit of scale there and um of course the fun things happen at the boundaries so across clusters and things like that um and all this is to say is when we have downtime somebody notices so uh January 14th of uh last year was not a super fun day this wasn't compute related but something that the ALF Squad actually had to deal with as well um and you can see there uh when we have downtime people notice and they are very vocal about it except I guess if you have a zoom um but yeah one of my favorite things to do there pop open Twitter whenever we have an outage which H luckily isn't that often but um
