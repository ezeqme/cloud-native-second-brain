---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Antonio Ojea", "Michelle Shepardson", "Benjamin Elder", "Google"]
sched_url: https://kccncna2024.sched.com/event/1hoxc/achieving-and-maintaining-a-healthy-ci-with-zero-test-flakes-antonio-ojea-michelle-shepardson-benjamin-elder-google
youtube_search_url: https://www.youtube.com/results?search_query=Achieving+and+Maintaining+a+Healthy+CI+with+Zero+Test+Flakes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Achieving and Maintaining a Healthy CI with Zero Test Flakes - Antonio Ojea, Michelle Shepardson & Benjamin Elder, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Antonio Ojea, Michelle Shepardson, Benjamin Elder, Google
- Schedule: https://kccncna2024.sched.com/event/1hoxc/achieving-and-maintaining-a-healthy-ci-with-zero-test-flakes-antonio-ojea-michelle-shepardson-benjamin-elder-google
- Busca YouTube: https://www.youtube.com/results?search_query=Achieving+and+Maintaining+a+Healthy+CI+with+Zero+Test+Flakes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Achieving and Maintaining a Healthy CI with Zero Test Flakes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxc/achieving-and-maintaining-a-healthy-ci-with-zero-test-flakes-antonio-ojea-michelle-shepardson-benjamin-elder-google
- YouTube search: https://www.youtube.com/results?search_query=Achieving+and+Maintaining+a+Healthy+CI+with+Zero+Test+Flakes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hl3jjCTTL50
- YouTube title: Achieving and Maintaining a Healthy CI with Zero Test Flakes - A. Ojea, M. Shepardson & B. Elder
- Match score: 0.891
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/achieving-and-maintaining-a-healthy-ci-with-zero-test-flakes/hl3jjCTTL50.txt
- Transcript chars: 32478
- Keywords: running, testing, actually, particular, failing, machine, infrastructure, failures, important, pretty, happening, instance, flakes, quality, looking, underlying, limits, across

### Resumo baseado na transcript

hello everybody we are going to talk about how to achieve and maintain a healthy CI with cedo test flakes what C can be an exaggeration but in the long term it is my name is Antonio o I work at Google inl in s testing and hi I'm Michelle sheperson I am a uh senior software engineer at Google and a chair of sick testingair testing hi I'm Benjamin aler uh I'm a chair of sick testing infra and I'm on the kuber steering committee okay okay let's let's

### Excerpt da transcript

hello everybody we are going to talk about how to achieve and maintain a healthy CI with cedo test flakes what C can be an exaggeration but in the long term it is my name is Antonio o I work at Google inl in s testing and hi I'm Michelle sheperson I am a uh senior software engineer at Google and a chair of sick testingair testing hi I'm Benjamin aler uh I'm a chair of sick testing infra and I'm on the kuber steering committee okay okay let's let's uh understand what is the problem we're going to talk about right FL it is that's the worst nightmare of every project maintainer every developer or we have dreams with that right F test is it passes sometimes other times doesn't pass and there are several combination of f right and several causes of flck test there can be environment problems because our infra is overwhelming and sometimes there can be that the test is lazy especially you are using goang go routines and channels and all this unlocks uh you know what I'm talking about right and the main problem is if it's flecky my Cod is it good or is it but and that's the the question that we make ourselves before the release can we release this uh project with all this test flaking or not our answer for that is clear no you cannot but how we achieve this well let's first understand better how kubernetes Project work right kubernetes uh project has a group uh special interest groups that can be horizontal or vertical horizontal means that the scope is across different areas and vertical means that they own some a specific area right SE testing usually people that comes to the project comes with the mapping of their Enterprises or companies or or organization and assume that se testing is the quality team well H spoiler alert it is not see testing is not about helping the other teams to write the test or review the test no it's in kubernetes every s owns their Cod owns their area and is in charge of collaborating with the other SS and understand the other six the goal of SE testing is provide the tooling provide the help provide the experience and this is how in kubernetes we collaborate each others to be able to achieve a uh a cedo flake policy we implemented the we also wrote down in our documentation that we have a c flake policies I think it was last year or something like that so there is a big commitment in each SE to not not allow flakes so how can you achieve that one of the common misconceptions is to invest in only in testing invest in only one area ri
