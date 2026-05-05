---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "SDLC"
themes: ["SDLC"]
speakers: ["Kyle Penfound", "Dagger"]
sched_url: https://kccncna2024.sched.com/event/1i7oY/youre-overpaying-for-ci-kyle-penfound-dagger
youtube_search_url: https://www.youtube.com/results?search_query=You%27re+Overpaying+for+CI+CNCF+KubeCon+2024
slides: []
status: parsed
---

# You're Overpaying for CI - Kyle Penfound, Dagger

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[SDLC]]
- Temas: [[SDLC]]
- País/cidade: United States / Salt Lake City
- Speakers: Kyle Penfound, Dagger
- Schedule: https://kccncna2024.sched.com/event/1i7oY/youre-overpaying-for-ci-kyle-penfound-dagger
- Busca YouTube: https://www.youtube.com/results?search_query=You%27re+Overpaying+for+CI+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre You're Overpaying for CI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7oY/youre-overpaying-for-ci-kyle-penfound-dagger
- YouTube search: https://www.youtube.com/results?search_query=You%27re+Overpaying+for+CI+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tsH3eTo2GLI
- YouTube title: You're Overpaying for CI - Kyle Penfound, Dagger
- Match score: 0.767
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/youre-overpaying-for-ci/tsH3eTo2GLI.txt
- Transcript chars: 34614
- Keywords: actually, dagger, running, request, pipeline, github, developer, checks, machines, change, pipelines, actions, environment, little, changes, minutes, machine, literally

### Resumo baseado na transcript

uh so hey everyone I'm Kyle um I'm with dagger thanks for the air horn Solomon um so I'm on the ecosystem team at dagger uh so what I do is basically look at all different CI pipelines all day long and figure out how they can work better um and as a kind of industry I think there's a lot of things we're doing wrong with CI uh so kind of my background before dagger I was released engineering Le to Hash cour for a while and then had

### Excerpt da transcript

uh so hey everyone I'm Kyle um I'm with dagger thanks for the air horn Solomon um so I'm on the ecosystem team at dagger uh so what I do is basically look at all different CI pipelines all day long and figure out how they can work better um and as a kind of industry I think there's a lot of things we're doing wrong with CI uh so kind of my background before dagger I was released engineering Le to Hash cour for a while and then had lots of other like devops and INF roles before that so I have lots of background in CI and now I get to just do CI all day so I get to form lots of opinions about it uh so today we're talking about your overpaying for CI where hopefully we're going to have lots of hot takes and as the takes get gradually hotter you can decide where you stop agreeing with me um so we'll see so here's my inspiration for today uh so the first two tweets by Solomon sitting right here in the third row so you can blame him uh is your over Pang for CI so there's our title right there um and kind of digging into more details uh he says your cicd pipeline should start on the developer's laptop if it only starts after a g push you're slowing your team down and throwing money down the drain C CSD shift left is the lowest hanging fruit for engineering efficiency for teams of 20 plus Engineers IMO so basically we have so many environments where we're not actually doing anything to to test our code before we push the CI and there's a lot of reasons for that that we'll talk about uh so that's Solomon's kind of luk warm take maybe medium not not quite a hot take uh but then we have uh this post from dhh that came out back in April about how they actually took all of their uh CI that was running in build kite uh and moved that back to developer machines because they realized actually if you run it on the super powerful like M3 Max or whatever he's talking about it's like twice as fast as he's running in Bill Kate uh so there's lots of trade-offs for that so that's like our our hyper hot take um and the reason that I decided to include this in in my talk today is because when I saw that back in April I was like okay that's nuts like no one else is going to do that but as someone who literally just thinks about CI all day the more I thought about it the more I'm like actually I think there's something there so we're going to dig into that we're going to talk about kind of the whole ramp up from your CI today to you know small steps along the way to get to maybe som
