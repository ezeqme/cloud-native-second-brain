---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["Security"]
speakers: ["Jeremy Rickard", "Ashna Mehrotra", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1i7oS/its-dangerous-to-build-it-alone-take-this-jeremy-rickard-ashna-mehrotra-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=It%27s+Dangerous+to+Build+It+Alone%2C+Take+This.+CNCF+KubeCon+2024
slides: []
status: parsed
---

# It's Dangerous to Build It Alone, Take This. - Jeremy Rickard & Ashna Mehrotra, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Salt Lake City
- Speakers: Jeremy Rickard, Ashna Mehrotra, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1i7oS/its-dangerous-to-build-it-alone-take-this-jeremy-rickard-ashna-mehrotra-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=It%27s+Dangerous+to+Build+It+Alone%2C+Take+This.+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre It's Dangerous to Build It Alone, Take This..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7oS/its-dangerous-to-build-it-alone-take-this-jeremy-rickard-ashna-mehrotra-microsoft
- YouTube search: https://www.youtube.com/results?search_query=It%27s+Dangerous+to+Build+It+Alone%2C+Take+This.+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UsHBGZ7np2Q
- YouTube title: It's Dangerous to Build It Alone, Take This. - Jeremy Rickard & Ashna Mehrotra, Microsoft
- Match score: 0.752
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/its-dangerous-to-build-it-alone-take-this/UsHBGZ7np2Q.txt
- Transcript chars: 32187
- Keywords: docker, images, container, source, vulnerabilities, registry, update, dependencies, pretty, actually, understand, version, upstream, artifacts, packages, package, practice, inside

### Resumo baseado na transcript

welcome to it's dangerous to build it alone take this I hope everybody likes Zelda um my name is Jeremy Rickard I'm a co-chair of Sig release in the kubernetes project I'm also a software engineer at Microsoft um my team helps build and produce the open- source software that's used inside of services like AKs um uh container industry stuff like that everyone my name is asna and I'm a software engineer at Microsoft and a Copa maintainer and today today we're going to be talking about some best

### Excerpt da transcript

welcome to it's dangerous to build it alone take this I hope everybody likes Zelda um my name is Jeremy Rickard I'm a co-chair of Sig release in the kubernetes project I'm also a software engineer at Microsoft um my team helps build and produce the open- source software that's used inside of services like AKs um uh container industry stuff like that everyone my name is asna and I'm a software engineer at Microsoft and a Copa maintainer and today today we're going to be talking about some best practices and tools to secure your supply chain so why are we here and why is this important so just in the past year there's been a lot of reports of vulnerabilities being exploited and it's important that we know what steps to take to mitigate this so there's a pretty good chance that at least a majority of the people in this room are doing some type of vulnerability management and while tools like Tri can help make you aware of vulnerabilities it's important that we actually understand and address them so one thing you can try to do is you can try to go to GitHub and ask for dependency updates and this is an example from the kubernetes release repo asking to bump the goang version because of a trivia report but scanners don't have a way to do any real type of analysis so you'll probably get a response like this saying that we can't do a dependency update just to satisfy a scanner another problem you can run into is you could be dependent on the Upstream binaries when they're no longer available so this example is from a older um C this example is from an older release RPM for kubernetes which is no longer available for upgrade so what do we do now to take the matter into our own hands and is there any guidance that we can lean on to figure out the right thing to do so today we're going to start by going over the secure supply chain consumption framework from the op ssf and it just outlines a bunch of best practices around consuming and using open- Source software so there's eight practices um that it outlines and we'll go over them and highlight some of the important ones and some of the tools you can use and the first practice is ingest it so this is just how are we going to consume The open- Source components so this means using public package managers using a open-source um binary repo manager solution and also mirroring our OSS source code into an internal location the next practice is scan it which is pretty straightforward it's using the open- source scanning
