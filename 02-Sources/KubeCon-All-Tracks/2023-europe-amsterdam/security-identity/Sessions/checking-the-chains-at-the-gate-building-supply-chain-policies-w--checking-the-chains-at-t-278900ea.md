---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["AI ML", "Security"]
speakers: ["Jeremy Rickard", "Microsoft"]
sched_url: https://kccnceu2023.sched.com/event/1Hya7/checking-the-chains-at-the-gate-building-supply-chain-policies-with-gatekeeper-and-ratify-jeremy-rickard-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Checking+the+Chains+at+the+Gate%3A+Building+Supply+Chain+Policies+with+Gatekeeper+and+Ratify+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Checking the Chains at the Gate: Building Supply Chain Policies with Gatekeeper and Ratify - Jeremy Rickard, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jeremy Rickard, Microsoft
- Schedule: https://kccnceu2023.sched.com/event/1Hya7/checking-the-chains-at-the-gate-building-supply-chain-policies-with-gatekeeper-and-ratify-jeremy-rickard-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Checking+the+Chains+at+the+Gate%3A+Building+Supply+Chain+Policies+with+Gatekeeper+and+Ratify+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Checking the Chains at the Gate: Building Supply Chain Policies with Gatekeeper and Ratify.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hya7/checking-the-chains-at-the-gate-building-supply-chain-policies-with-gatekeeper-and-ratify-jeremy-rickard-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Checking+the+Chains+at+the+Gate%3A+Building+Supply+Chain+Policies+with+Gatekeeper+and+Ratify+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pj8Q8nnMQWM
- YouTube title: Checking the Chains at the Gate: Building Supply Chain Policies with Gatekeeper & Ratify - J Rickard
- Match score: 1.004
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/checking-the-chains-at-the-gate-building-supply-chain-policies-with-ga/pj8Q8nnMQWM.txt
- Transcript chars: 36053
- Keywords: cluster, gatekeeper, policy, ratify, policies, external, verifier, provider, registry, pretty, s-bomb, labels, write, images, cosine, workflow, verify, running

### Resumo baseado na transcript

welcome to checking the chains at the gate we're going to talk about how we can build supply chain security policies using gatekeeper and a project called ratify my name is Jeremy this is probably my favorite contribution to kubernetes it's my cat with a laser background he was the 120 release mascot I was a 120 release date so that was the fun perk you get for being really Slade you get to come up with a fun mascot I'm also a chair in Sig release and I'm also

### Excerpt da transcript

welcome to checking the chains at the gate we're going to talk about how we can build supply chain security policies using gatekeeper and a project called ratify my name is Jeremy this is probably my favorite contribution to kubernetes it's my cat with a laser background he was the 120 release mascot I was a 120 release date so that was the fun perk you get for being really Slade you get to come up with a fun mascot I'm also a chair in Sig release and I'm also in the kubernetes code conduct committee so you may know me from one of those things in my day job I am an engineer on the Azure container Upstream team and we are really focused on making sure that open source and Microsoft have a good time together especially specifically around containers we're looking at things in the supply chain security space and making sure that we are doing good things with open source and helping open source be successful as well before we get going let's kind of take a moment to pause and reflect on the state of building and shipping services and software today it's pretty good there's a lot of tools that we can use a lot of languages a lot of Frameworks that we can take dependencies on to just satisfy the the needs and allow us to focus on business use cases right we don't have to go and reinvent the wheel all the time sometimes we do but not all the time uh and generally it just makes things faster the downside to that is that there's a lot of things there's a lot of complexity to worry about Building Services is is easier than it probably has been in a long time but operating those services and knowing what's running in different places is a little more complicated than it used to be as we start building micro services and shipping things to more and more clusters and different clouds it's really difficult to kind of understand what am I doing in Cloud a and Cloud B what's this you I've got between those things how do I keep track how do I enforce that we're doing things consistently across those things and to make matters worse a lot of governments are helping us by making new regulations and directives that we have to comply with the EU this is an example uh has has mandated that people start to produce s-bombs the US government has done the same thing we at Microsoft have had to react and start to build s-bombs for Windows like think about the the complexity that comes into that and all of that happens on top of the existing complexities and the difficulties we have
