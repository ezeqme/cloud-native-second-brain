---
type: session
event: "PromCon EU 2025"
year: 2025
kind: session
youtube_url: "https://www.youtube.com/watch?v=UW-BZn_F1Lo"
youtube_id: "UW-BZn_F1Lo"
playlist: "PromCon EU 2025"
playlist_id: "PLj6h78yzYM2P534LgwCVm3GQdxLcSt7We"
playlist_index: 40
speakers: ["Mirek Chocholous"]
topics: ["Metrics", "Logging", "Kubernetes", "AI Observability"]
keywords: ["manager", "clusters", "cluster", "log", "prometheus", "metrics", "simply", "particular", "server", "issues", "source", "simple", "questions", "receiver", "alerts", "another", "quorum", "deployment", "notification", "knowledge", "gracefully", "amnesia", "receive", "failed"]
transcript_file: "_sources/transcripts/youtube-playlists/promcon-eu-2025/lightning-talk-alert-quorum-universal-aggregator/UW-BZn_F1Lo.txt"
transcript_chars: 5081
status: "transcript-downloaded"
match_score: 1.08
---

# Lightning Talk: Alert Quorum Universal Aggregator - AQUA - Mirek Chocholous

## Metadata

- YouTube: https://www.youtube.com/watch?v=UW-BZn_F1Lo
- Playlist: PromCon EU 2025
- Speakers: Mirek Chocholous
- Topics: [[Metrics]], [[Logging]], [[Kubernetes]], [[AI Observability]]

## Transcript

Hello. Uh I'm Merrick from CDN77. Uh and uh I've got a problem to ask simple questions. So this talk is basically I will ask you three simple questions in the end but I have to go to them. Uh first uh I will not speak about I I will speak about u Aqua that is in the in the uh subject of this talk but I have to go there. Uh first thing first uh everyone here is using alert manager I guess in some kind of uh deployment and everyone knows what alert manager is doing. Alert manager simply uh gives a notification about every alert. Uh it uh somehow understands which alert are new one and uh which are already known and per each receiver it sends the notification. uh it tracks if the particular receiver was successfully sent or not yet. Uh it works nice but this description only applies uh to single node alert manager. If you want to go to cluster it is a little bit different. Uh yep there is one more line.

Uh in the cluster mode uh the alert manager nodes uh simply talk to each other and they keep the knowledge about what alerts were already notified and which weren't to particular uh particular receiver. Uh as a bonus for that how it is doing uh for each alert it is uh partic uh doing fingerprint which is simply hash of all the uh labels that are for a particular alert. Um here that's how it should work and I would love if it would work like that. The thing is it works well until it doesn't uh when it doesn't work when particular node uh is rebooted not gracefully. uh there is a talk tomorrow about it uh about the amnesia of alert manager and uh yeah I don't want to jump into that topic because definitely there will be more details uh there are like five issues on the on the GitHub tracker for that and yeah um it simply that's the state when uh you simply shut down the art manager and start it gracefully there is an log it works nicely but when when [ __ ] hits the fan uh it it doesn't work Uh so uh another another problem is if you get have multiple alert manager nodes the more you got of them the more often you receive uh instead of simple okay message you receive a combo of okay fail okay because they have to speak to each other and one of the one of the nodes doesn't know that it is okay.

So for him it still failed. So he has the need to tell you it failed and then yeah it's okay. Uh another thing is that the uh uh supported deployment for Prometheus and for Victoria metrics is that you are notifying all the alert manager nodes that you've got. you are shipping from all your monitoring clusters in our case in CD and Simpson we've got five clusters all over the world in in different continents and one more uh that are uh shipping the alerts to uh alert managers all of them and the more often it's happening it sucks because our uh owner company owner and founder uh he likes the bus of the alerts so his phone still is receiving all the SMS for a server down and yeah I'm responsible for monitoring so you can imagine you can imagine uh it's sometimes difficult uh so I wanted to fix that and how to fix that uh you've got five clusters it's ideal for you to have there some quorum you uh don't want to uh say that some server is down when you cannot ping it from Amsterdam when the server is in Hong Kong.

It's not relevant. So yeah, uh other issues of al manager, sorry. Um uh alert manager as it is, it doesn't support uh rate limits. So if one of those issues that I mentioned like flipping all the knowledge and like the amnesia, it's flipping the status of all the a [ __ ] sorry. Uh so uh it doesn't have the rate limits. uh it doesn't have the column so you have to uh write something else. What we wrote? We wrote some tool that is fetching the alert managers like bunch of them. It managing some some code room. It's uh you processing based on some scripts that you define. uh if the alert is new, if it's resolved, uh it's uh sending the the customized messages and with that you may even write some uh some messages that are like server down five servers in Frankfurt and some samples of the IPs because you don't want to send SMS for each server when your company owner is receiving all the SMSs. Um and yeah, it has the rate limit.

Uh uh yeah uh it's running in ah sorry yeah thank you my >> at least at least let me ask my questions is there some open source tool that is supposed to send the correct notifications not all the notifications as art manager is doing it because the flipped ones uh simply suck and everyone is uh like angry about it and is there some open source tool like that? Uh should we open source it because like my feeling is that everyone has to already face this issue. >> All right. Uh so please open source this. Uh I don't think there's anything like this. Um and I think it'll help scale alert manager but I'm sorry to cut you off. Uh and if anyone is also having issues around alert manager like we are seeing a constant uh theme of things. So we'll discuss it at the dev summit on Thursday and maybe we can all come up with a plan for alert manager. Thank you. Yeah. All right. We have


## Related keywords

[[manager]] [[clusters]] [[cluster]] [[log]] [[prometheus]] [[metrics]] [[simply]] [[particular]] [[server]] [[issues]] [[source]] [[simple]]

## Notes

- Raw note imported from CNCF YouTube playlist. Promote durable insights to topic notes under `03-Topics/`.
