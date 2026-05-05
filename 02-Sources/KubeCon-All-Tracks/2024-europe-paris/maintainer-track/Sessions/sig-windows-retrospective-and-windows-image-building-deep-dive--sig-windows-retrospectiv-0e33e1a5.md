---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Claudiu Belu", "Cloudbase Solutions"]
sched_url: https://kccnceu2024.sched.com/event/1YhiZ/sig-windows-retrospective-and-windows-image-building-deep-dive-claudiu-belu-cloudbase-solutions
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Windows+Retrospective+and+Windows+Image+Building+Deep+Dive+CNCF+KubeCon+2024
slides: []
status: parsed
---

# SIG Windows Retrospective and Windows Image Building Deep Dive - Claudiu Belu, Cloudbase Solutions

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Claudiu Belu, Cloudbase Solutions
- Schedule: https://kccnceu2024.sched.com/event/1YhiZ/sig-windows-retrospective-and-windows-image-building-deep-dive-claudiu-belu-cloudbase-solutions
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Windows+Retrospective+and+Windows+Image+Building+Deep+Dive+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre SIG Windows Retrospective and Windows Image Building Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhiZ/sig-windows-retrospective-and-windows-image-building-deep-dive-claudiu-belu-cloudbase-solutions
- YouTube search: https://www.youtube.com/results?search_query=SIG+Windows+Retrospective+and+Windows+Image+Building+Deep+Dive+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iR6sIf5UOX0
- YouTube title: SIG Windows Retrospective and Windows Image Building Deep Dive - Claudiu Belu, Cloudbase Solutions
- Match score: 0.87
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sig-windows-retrospective-and-windows-image-building-deep-dive/iR6sIf5UOX0.txt
- Transcript chars: 27930
- Keywords: windows, images, basically, essentially, server, container, simply, docker, especially, course, manifest, couple, useful, version, interesting, issues, another, layers

### Resumo baseado na transcript

uh hello everyone thanks for joining for uh Sig Windows maintainer talk uh my name is cloud bellu uh I am a senior Cloud engineer at cloudbased Solutions and I am one of the tech leads for Sig windows and we are going to do a very short retrospective of uh what happened uh from the last cycle and some additional guides on how to build Windows images uh different tips and tricks and some very uh tricks that you could use uh this came up because um there are

### Excerpt da transcript

uh hello everyone thanks for joining for uh Sig Windows maintainer talk uh my name is cloud bellu uh I am a senior Cloud engineer at cloudbased Solutions and I am one of the tech leads for Sig windows and we are going to do a very short retrospective of uh what happened uh from the last cycle and some additional guides on how to build Windows images uh different tips and tricks and some very uh tricks that you could use uh this came up because um there are quite a few uh questions regarding how to build the best Windows images you can possibly do so that's why uh I'm here we've been doing this for a couple of years so we have a bit of knowledge and experience regarding this and in the end U I'm going to try to recruit you recruit you to join Sig windows we are a fun loving community so you're always uh welcome to join us so minor updates uh um we welcome amim naan from broadcom as one of our new tech leads for S Windows he worked a lot on Windows operation operational Readiness which is practical standard of um tests and things which should pass and work properly uh in any Windows environment to certify that indeed it's working as intended and properly and he also worked for uh Windows death tools which are very useful to getting new contributors into kubernetes space and especially for Windows and we thank Jay Vias for all his contrib contributions he has been a great help for us and he has been a very pleasant um Presence at any conference and meetings and so on one other important thing to note is that the no log query feature will be entering beta in 130 we have a couple of other updates uh we've been improving the windows operation Readiness and windows death tools and we have a few other things in the pipeline so they're not yet ready to be announced though but let's go to the main thing for today which is the windows image building Deep dive so a little bit of context um what we're going to see here we basically added a lot of um window support for a lot of KU images the pause image the C proxy image the CN CSI and so on so in most scenarios we basically had to integrate those images into whatever uh build processes kubernetes already had so there were quite a few restrictions on how we were going to build the images but we're going to go from scratch from zero from the most basic images that you could possibly build to more complex which are currently employed in kubernetes image building processes and release processes Okay so one important thing
