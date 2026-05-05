---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["AI ML", "Security"]
speakers: ["Adolfo García Veytia", "Carlos Panato", "Chainguard"]
sched_url: https://kccnceu2023.sched.com/event/1Hydq/secure-your-project-with-the-sig-release-supply-chain-kit-adolfo-garcia-veytia-carlos-panato-chainguard
youtube_search_url: https://www.youtube.com/results?search_query=Secure+Your+Project+with+the+SIG+Release+Supply+Chain+Kit+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Secure Your Project with the SIG Release Supply Chain Kit - Adolfo García Veytia & Carlos Panato, Chainguard

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Adolfo García Veytia, Carlos Panato, Chainguard
- Schedule: https://kccnceu2023.sched.com/event/1Hydq/secure-your-project-with-the-sig-release-supply-chain-kit-adolfo-garcia-veytia-carlos-panato-chainguard
- Busca YouTube: https://www.youtube.com/results?search_query=Secure+Your+Project+with+the+SIG+Release+Supply+Chain+Kit+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Secure Your Project with the SIG Release Supply Chain Kit.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hydq/secure-your-project-with-the-sig-release-supply-chain-kit-adolfo-garcia-veytia-carlos-panato-chainguard
- YouTube search: https://www.youtube.com/results?search_query=Secure+Your+Project+with+the+SIG+Release+Supply+Chain+Kit+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AwzrMnxQ6c4
- YouTube title: Secure Your Project with the SIG Release Supply Chain Kit - Adolfo García Veytia & Carlos Panato
- Match score: 0.845
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/secure-your-project-with-the-sig-release-supply-chain-kit/AwzrMnxQ6c4.txt
- Transcript chars: 22210
- Keywords: release, github, generate, artifacts, binary, software, called, actions, another, inside, projects, binaries, cosine, supply, working, thinking, started, signed

### Resumo baseado na transcript

thanks for coming to our talk we're gonna talk about the secure your project with cigar release supply chain kit yeah hello my name is um Adolfo Garcia and I am one of the tech leads with kubernetes release I work at a company called changard and we do supply chain security and I also do other stuff like besides working with Carlos and Sig release I also stayed on the K native student committee I am one of the contributors to the spdx as from standard and I have

### Excerpt da transcript

thanks for coming to our talk we're gonna talk about the secure your project with cigar release supply chain kit yeah hello my name is um Adolfo Garcia and I am one of the tech leads with kubernetes release I work at a company called changard and we do supply chain security and I also do other stuff like besides working with Carlos and Sig release I also stayed on the K native student committee I am one of the contributors to the spdx as from standard and I have been working on the kubernetes really stooling for a while now and my name is Carlos I also work at chenguard I'm member of the kubernetes steering committee and also Tech lead on the cigarilli side and contributor to other programs inside kubernetes also I'm a maintainer of six store and that's it so um before we start I would like just a small order of business so contrary to popular belief we are not the same person and I I mean none of those mind when Carlos when I'm flattered by being called Carlos or he is insulted by cold porca but not the same person all right um so um uh before we start I would like to talk about the origins of the projects that we're going to be talking about so we are sick release and we are the release engineering team is uh the outfit responsible for creating the tooling that releases kubernetes after each each cycle so whenever you see one new batch release or one of the minor release of current kubernetes getting cut it's also behind it and it's our tooling that does it and the way we do it is we have this big monolith binary that we run to cut the releases and it takes care of a bunch of stuff it builds kubernetes the binaries the images it builds the system packages now it pushes the artifacts to the Registries to GitHub all of the GitHub objects like tags get get taken care by that binary and it also creates a release node and then well you know now it's handling the the generation of the supply chain security artifacts that we publish with every release so a lot of work goes into this tooling it's like several thousand probably lines of Code by now and we for a while we have been thinking that all of this work cannot go to waste by just applying it to kubernetes so the first thing that we started doing was considering how can we help other projects on the kubernetes organization get uh the benefit of this but now we're also thinking well this is like Journal purpose software that other other projects can profit from so the binary I was talking about is called cra
