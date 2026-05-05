---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Security + Identity + Policy"
themes: ["AI ML", "Security"]
speakers: ["Parth Patel", "Michael Lieberman", "Kusari"]
sched_url: https://kccncna2022.sched.com/event/182Jo/slsa-frsca-recipe-for-secure-supply-chain-parth-patel-michael-lieberman-kusari
youtube_search_url: https://www.youtube.com/results?search_query=SLSA+FRSCA+Recipe+For+Secure+Supply+Chain+CNCF+KubeCon+2022
slides: []
status: parsed
---

# SLSA FRSCA Recipe For Secure Supply Chain - Parth Patel & Michael Lieberman, Kusari

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Detroit
- Speakers: Parth Patel, Michael Lieberman, Kusari
- Schedule: https://kccncna2022.sched.com/event/182Jo/slsa-frsca-recipe-for-secure-supply-chain-parth-patel-michael-lieberman-kusari
- Busca YouTube: https://www.youtube.com/results?search_query=SLSA+FRSCA+Recipe+For+Secure+Supply+Chain+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre SLSA FRSCA Recipe For Secure Supply Chain.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Jo/slsa-frsca-recipe-for-secure-supply-chain-parth-patel-michael-lieberman-kusari
- YouTube search: https://www.youtube.com/results?search_query=SLSA+FRSCA+Recipe+For+Secure+Supply+Chain+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pZzQHLPNh-U
- YouTube title: SLSA FRSCA Recipe For Secure Supply Chain - Parth Patel & Michael Lieberman, Kusari
- Match score: 0.769
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/slsa-frsca-recipe-for-secure-supply-chain/pZzQHLPNh-U.txt
- Transcript chars: 31296
- Keywords: running, tecton, actually, pipeline, security, secure, itself, environment, little, chains, signed, everything, happening, exactly, looking, production, workload, allows

### Resumo baseado na transcript

good afternoon everyone good evening we're we're very close to the evening time um so we're going to be speaking about today is fresa an open source project um so real quick before we start off a quick introduction about ourselves um so I'm one of the co-founders of kusari a supply chain security company and some of the focuses we have is you know building secure artifacts as well as answering the hard question of you know what exactly am I ingesting before that I was an Solutions architect

### Excerpt da transcript

good afternoon everyone good evening we're we're very close to the evening time um so we're going to be speaking about today is fresa an open source project um so real quick before we start off a quick introduction about ourselves um so I'm one of the co-founders of kusari a supply chain security company and some of the focuses we have is you know building secure artifacts as well as answering the hard question of you know what exactly am I ingesting before that I was an Solutions architect in regulated Industries as well as commercial settings um and I'm a maintainer on various open source projects like intoto ad stations intoto goang fresa and guac I'm GNA hand it out to my colleague to int introduce himself and continue with the presentation uh I'm Mike liberman um I'm also a co-founder of gusari um I mostly uh past several years I've been an architect with a focus on supply chain security um a little bit few other details about myself um I'm ass salsa steering commit member for folks who are you know familiar with salsa the the um secure uh the supply chain security framework I'm also a tag security lead for the cncf and I also helped co-lead the secure software Factory reference architecture from the cncf all right so we're going to talk a little bit about uh the threats um you know just supply chain security threats and how uh fresa helps out with that um we're going to talk about you know secure software Factory reference architecture we'll talk about fresa itself um and we'll talk about mapping the components and we'll also give a little bit of a a demo on fresa uh and also one thing just to note is fresa is an open ssf project underneath the uh Linux foundation so this is uh the threat um diagram that came from salsa and so there's a lot of different things kind of going on in here right you can have threats coming from the developer threats uh in your source code repository threats coming in from dependencies from your package manager and all sorts of different places fresa is um if we kind of look at it a level in uh here Fresca is uh focused around build security right and the specific threats that it's focused on is you know the inputs into the build making sure that you know are we running um what we expect to be running uh The Bu itself like is somebody actually actively getting into the build and um compromising stuff as it's building and then also verifying that hey is the thing I'm is the thing I'm looking at the thing I actually built an
