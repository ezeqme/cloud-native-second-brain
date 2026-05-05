---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Alexander Buck", "Tomas Aschan", "Spotify"]
sched_url: https://kccnceu2026.sched.com/event/2CW0Y/moving-spotifys-infrastructure-management-up-the-stack-from-kubebuilder-to-kro-and-k-poperator-alexander-buck-tomas-aschan-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Moving+Spotify%E2%80%99s+Infrastructure+Management+Up+the+Stack+from+Kubebuilder+to+Kro+and+K-poperator+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Moving Spotify’s Infrastructure Management Up the Stack from Kubebuilder to Kro and K-poperator - Alexander Buck & Tomas Aschan, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alexander Buck, Tomas Aschan, Spotify
- Schedule: https://kccnceu2026.sched.com/event/2CW0Y/moving-spotifys-infrastructure-management-up-the-stack-from-kubebuilder-to-kro-and-k-poperator-alexander-buck-tomas-aschan-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Moving+Spotify%E2%80%99s+Infrastructure+Management+Up+the+Stack+from+Kubebuilder+to+Kro+and+K-poperator+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Moving Spotify’s Infrastructure Management Up the Stack from Kubebuilder to Kro and K-poperator.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW0Y/moving-spotifys-infrastructure-management-up-the-stack-from-kubebuilder-to-kro-and-k-poperator-alexander-buck-tomas-aschan-spotify
- YouTube search: https://www.youtube.com/results?search_query=Moving+Spotify%E2%80%99s+Infrastructure+Management+Up+the+Stack+from+Kubebuilder+to+Kro+and+K-poperator+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=W-_kJEX-_RY
- YouTube title: Moving Spotify’s Infrastructure Management Up the Stack from Kubebu... Alexander Buck & Tomas Aschan
- Match score: 0.889
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/moving-spotifys-infrastructure-management-up-the-stack-from-kubebuilde/W-_kJEX-_RY.txt
- Transcript chars: 29740
- Keywords: platform, resource, resources, spotify, feature, operator, products, actually, infrastructure, cluster, internal, developer, controller, product, features, iceberg, management, declarative

### Resumo baseado na transcript

Hello everybody and uh welcome to this spa talk about how Spotify is moving our infrastructure management up the stack. I'm Thomas >> and I'm Alex and we're both very happy that you are taking the time to sit down here with us instead of getting in line early for beers after. Um, in their talk they recaped the history of infrastructure management at Spotify and then highlighted a few problems we were working on solving. For batch processing jobs, GCS is a great fit, but it's also useful to be able to run SQL over that data for ad hoc queries and dashboarding use cases, in which case BigQuery is better a better fit. To enable these use cases, we typically have jobs that copy the data from GCS to BigQuery, but that leads to significant duplication. Apache iceberg is an open table specification allowing an abstraction between the underlying storage and the processing engine.

### Excerpt da transcript

Hello everybody and uh welcome to this spa talk about how Spotify is moving our infrastructure management up the stack. I'm Thomas >> and I'm Alex and we're both very happy that you are taking the time to sit down here with us instead of getting in line early for beers after. Uh we work in a team at Spotify who are building our internal resource management platform which we call declarative infra. And building a resource management platform means we provide tooling for feature teams that is the teams who actually build the Spotify product to configure their infrastructure in code in their source repositories and have that configuration turned into actual cloud resources. But at Spotify, we also have a lot of teams who build our internal developer platform. And some of them build bespoke products that don't have an off-the-shelf thing that we can just use. And others take care of the usage of our off-the-shelf products across the organization. So for example, developing best practices for data storage or running cost optimization programs and so on.

Our team serves both these personas, the feature teams and the platform teams. And we want platform teams to be able to expose their products to the feature teams so that they can use a single configuration surface for all of their infrastructure needs where it's whether it's an off-the-shelf product or an internal thing. In other words, we want to provide feature teams with less complex and more powerful abstractions and allow platform teams to evolve their products independently. We are picking up where our colleagues Oliver, who's sitting right here, and Frederick, who's on parental leave, left off at CubeCon North America in the fall. um where they shared our ambition to and our strategy to manage 1 million resources internally and we just recently reached that milestone by the way. Um show of hands how many of you have seen that talk either live at CubeCon or on YouTube after like three. Okay, there's a link here so you can go watch it but please don't follow that until after this talk. Um, in their talk they recaped the history of infrastructure management at Spotify and then highlighted a few problems we were working on solving.

And today we're going to zoom in on one of those. Namely, how do we empower platform teams at Spotify to build powerful batteriesinccluded infrastructure products and then put them in the hands of feature teams in ways that let the platform teams focus on their products rather t
