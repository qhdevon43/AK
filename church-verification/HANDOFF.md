# HANDOFF.md — Church Worship-Culture Verification (extraction only)

Frame grids: ALL timestamps burned into tiles are TRUE video time (grids were
composed from YouTube storyboard frames with absolute timing) — no offsets needed.
Baseline grids: 1 frame/60s. Dense grids: 1 frame/~10s (native storyboard interval).
Transcripts are YouTube 'en-orig' auto-captions (ASR), not Whisper — see PIPELINE_REPORT.md.


---

## Movement Church (Celina, TX) — Covenant Living - Your New Name (4F7R_XFsAHU)

### 1. Manifest
```json
{
  "church": "Movement Church (Celina, TX)",
  "video_id": "4F7R_XFsAHU",
  "url": "https://www.youtube.com/watch?v=4F7R_XFsAHU",
  "title": "Covenant Living - Your New Name",
  "upload_date": "20260713",
  "duration_seconds": 6194,
  "whisper_model_used": "none \u2014 YouTube 'en-orig' auto-captions (ASR) substituted; Whisper impossible (media download blocked in sandbox, see PIPELINE_REPORT.md)",
  "notes": "metadata via yt-dlp web_embedded client (datacenter IP bot-check workaround); livestream release 2026-07-12T13:55:02Z"
}
```

### 2. Segments
```json
{
  "segments": [
    {
      "start": "00:00:00",
      "end": "00:04:50",
      "label": "other",
      "confidence": "high",
      "note": "pre-service countdown"
    },
    {
      "start": "00:04:50",
      "end": "00:26:00",
      "label": "worship",
      "confidence": "high"
    },
    {
      "start": "00:26:00",
      "end": "00:31:30",
      "label": "prayer",
      "confidence": "medium",
      "note": "exhortation on the blood / God's love, ends in corporate prayer"
    },
    {
      "start": "00:31:30",
      "end": "00:35:30",
      "label": "announcements",
      "confidence": "high",
      "note": "welcome, connection card, building/school vision, giving"
    },
    {
      "start": "00:35:30",
      "end": "01:25:40",
      "label": "message",
      "confidence": "high",
      "note": "Covenant Living - Your New Name (Abram/Abraham)"
    },
    {
      "start": "01:25:40",
      "end": "01:36:00",
      "label": "worship",
      "confidence": "high",
      "note": "response song 'In the Name'"
    },
    {
      "start": "01:36:00",
      "end": "01:43:14",
      "label": "ministry_time",
      "confidence": "medium",
      "note": "corporate declarations over needs, prayer team called up, closing worship"
    }
  ],
  "worship_minutes": 31.5,
  "message_minutes": 50.2,
  "ministry_minutes": 7.2,
  "worship_to_total_ratio": 0.305
}
```

### 3. Speech density (worship + ministry buckets only; 5-min buckets, ASR word counts)
```
00:00–05:00 | 34 words
05:00–10:00 | 483 words
10:00–15:00 | 505 words
15:00–20:00 | 360 words
20:00–25:00 | 275 words
25:00–30:00 | 735 words
1:25:00–1:30:00 | 478 words
1:30:00–1:35:00 | 478 words
1:35:00–1:40:00 | 671 words
1:40:00–1:43:14 | 197 words
```

### 4. Contact sheets (timestamps in tiles are true video time)
```
grid_baseline_01.jpg
grid_baseline_02.jpg
grid_baseline_03.jpg
grid_baseline_04.jpg
grid_baseline_05.jpg
grid_baseline_06.jpg
grid_baseline_07.jpg
grid_dense_ministry_01.jpg
grid_dense_ministry_02.jpg
grid_dense_ministry_03.jpg
grid_dense_worship_tail_01.jpg
grid_dense_worship_tail_02.jpg
grid_dense_worship_tail_03.jpg
grid_dense_worship_tail_04.jpg
grid_dense_worship_tail_05.jpg
grid_dense_worship_tail_06.jpg
```

### 5a. Transcript excerpt — final 10 min of worship

```
00:16:03  We will [music] trust you and believe.
00:16:08  Let [music and singing] it be. You alone will be a fine foundation. [music and singing]
00:16:15  And what you spokeen is enough. And it's the crown [singing] we're
00:16:20  standing on. You are God. And we [music] will not be shen.
00:16:28  Oh, [music] we will trust you and [singing] believe. As it's written,
00:16:34  let it [music] be. Cuz you alone [singing] will be a firm
00:16:38  foundation.
00:16:42  >> What [music] is enough is a crown we're [singing] standing on. You
00:16:48  are God [music] and we will not [singing] be shen. [music]
00:16:58  You keep [music] your promises [singing]
00:17:03  never [music] end. Your goodness is never [music] >> from generation
00:17:10  >> from generation
00:17:14  to generation. [music]
00:17:17  And you keep your cup [singing] for your faithfulness.
00:17:25  [music] [singing] Faithfulness generation. [music] From generation to
00:17:32  generation [singing] to generation generation [music] generation
00:17:40  to generation [music] generation >> generation
00:17:46  to gener
00:17:50  >> [music] >> Oh, we thank you for your faithful name. Oh, we thank
00:17:57  you.
00:18:00  Hey.
00:18:04  Come on, lift your hands and just worship him this morning. We
00:18:07  thank you, Lord. He's a faithful [music] God. Oh, we worship you,
00:18:13  Jesus.
00:18:16  We worship you Lord.
00:18:21  Thank you Lord.
00:18:28  What has [singing] washed away [music] my s?
00:18:35  Nothing [music and singing] but the blood of Jesus [music] and
00:18:43  what has [singing] made me whole again.
00:18:50  Nothing [singing] [music] but the blood of Jesus. [singing]
00:18:59  >> [music]
00:19:04  >> Oh, and [singing] what has [music] washed away my [singing] sin?
00:19:12  Nothing but the [music] blood of [singing] Jesus.
00:19:19  And what [music] has made me whole [singing] again? [music]
00:19:27  Nothing but the blood of Jes. [music] [singing]
00:19:36  [music]
00:19:39  [singing]
00:19:42  Nothing [music] but the blood of Jesus. [singing and music]
00:19:50  has made me whole again. [music and singing] We sing nothing
00:19:57  but the light of Jesus. [music] [singing] And
00:20:05  [music] preious is [singing] the love [music] that
00:20:13  makes me [music] white [singing] as snow.
00:20:21  [singing] I [music] know nothing but [singing] the blood
00:20:29  of Jesus. [music] Operation
00:20:35  precious is [music and singing] thous
00:20:42  [music] [singing]
00:20:53  [singing] [music]
00:20:57  [singing] of [music] Jesus.
00:21:07  Thank you for your love.
00:21:11  [music and singing] Thank you for your love.
00:21:15  [music]
00:21:20  >> [singing]
00:21:23  [music] >> Oh, I thank you.
00:21:30  Oh, precious. [music] Preious [singing] is
00:21:37  [music] the love that makes me [music] white
00:21:45  as [singing] snow.
00:21:50  >> [music and singing] >> bound
00:21:55  [music] nothing but the [singing] blood of Jesus.
00:22:02  And how [music] [singing] precious is the blood
00:22:10  [music] that [singing] makes me white as [music and singing] snow. Oh
00:22:18  no other [music] found [singing]
00:22:25  nothing [music] but the blood of [singing] Jesus.
00:22:33  [singing]
00:22:37  Oh nothing but the blood [music] Jesus. Oh, come on [singing] church.
00:22:43  We thank you for his love. [music]
00:22:48  We thank you [singing] for
00:22:52  your love. >> Thank you for your [music]
00:22:59  [singing] sing. So precious and [music] preious
00:23:07  is [singing] the glow that makes me [music]
00:23:15  white as [singing] snow. [music]
00:23:23  I know nothing [singing] but the blood of [music] Jesus.
00:23:32  [singing]
00:23:39  >> There's nothing but the blood. [music and singing] >> There's nothing but the blood
00:23:49  for those [music] who worship you. We [singing] thank you. We praise
00:23:53  you, Lord.
00:24:01  >> We thank you for your
00:24:12  love. Thank you. [music] Thank you, [singing] Lord. Thank you, Lord. Come
00:24:19  on, church. One more time, let's just lift our hands and [music]
00:24:22  say thank you. >> Oh, he [singing] really came [music]
00:24:30  for us. So we [music and singing] say thank you Lord. We say
00:24:37  [music and singing] thank you. We say thank [music] you.
00:24:46  We [singing and music] say thank you.
00:24:53  Say [singing] thank you.
00:25:01  Thank you Jesus.
00:25:08  >> Thank you Jesus [music and singing] for
00:25:21  Jesus. Just stay in this position of worship, this place of worship.
00:25:30  Tap into the presence of God.
00:25:36  >> We thank you, Lord. We acknowledge your presence today. We say yes
00:25:43  to you today. We move with you today, Holy Spirit.
00:25:50  Thank you, Lord. We thank you, Lord.
00:25:56  You know, we serve a God who is [music] the same yesterday,
```

### 5b. Transcript excerpt — ministry time (entirety)

```
01:36:04  >> Oh let's praise him for it now. All that's left is to
01:36:08  praise it. That's all that's left. The work has been done. We
01:36:13  don't have to strive or worry or fret. It's over. >> Oh, thank
01:36:21  you, Lord.
01:36:24  You say, "Pastor, does that mean it's a ceasefire?" No. I'm declaring
01:36:28  it's over.
01:36:31  >> The attack is over. It's done. It's dead. It's been wiped out.
01:36:41  You know, that's what the enemy has to be. You got to
01:36:44  deal with the enemy. There is no negotiation with the devil. There's
01:36:50  no negotiation with cancer, with anxiety or fear. Well, I'm just learning
01:36:55  to cope. Pastor, you need to eradicate that from your life.
01:37:02  >> You need to be just like April. Not this guy. Not anymore.
01:37:08  I'm a covenant man. >> I have a covenant with God. I'm Abraham.
01:37:14  I'm Abraham. I don't care what I used to be. And he
01:37:18  said, now listen to me now. He said it before he had
01:37:21  the promised child.
01:37:27  He said it before he had it. That's what faith does. Faith
01:37:32  declares the end from the beginning. That's what we just did.
01:37:40  We just used our new covenant name, the name above every other
01:37:44  name. Amen. >> That at the name of Jesus, every knee has to
01:37:50  bow. Live your life in your covenant.
01:37:59  Use your new name.
01:38:03  Don't act like a a person without a covenant. Don't act like
01:38:06  you're a stranger to the covenant. It's a promise. Know your covenant.
01:38:12  You read the word of God. You see that promise. You're like,
01:38:19  you know what I mean by that? That's me. He just said
01:38:22  it. He just gave it. That's a promise. It's mine. That's not
01:38:27  who I am anymore. I'm not a fearful person any longer. Stop
01:38:30  saying it. That's be like Abraham saying, "I'm not the father of
01:38:34  many. I'm not the father of many. I'm not the father of
01:38:36  many." He didn't say that. He said, "I'm the father of many."
01:38:40  It's who I am now. I got a covenant name. You have
01:38:44  a covenant name. You got your name changed, too. You are baptized
01:38:49  into Christ. You're in covenant with God. Amen. Father, in the name
01:38:54  of Jesus, oh, the name above every other name. Thank you, Lord,
01:38:59  for our covenant. Thank you, Lord, that we are redeemed. Our freedom
01:39:05  has been purchased and we no longer have to live as people
01:39:10  without a covenant with you. We can live in our covenant. Thank
01:39:14  you, Lord, for what you've done 2,000 years ago. Not even what
01:39:20  this morning, but the work was done 2,000 years ago. I thank
01:39:23  you, Lord, for the revelation today that we got on what you've
01:39:27  already done. the revelation on our new name. And I thank you,
01:39:32  Lord, that we will be a people from this moment on who
01:39:36  will not be considering ourselves as people without a covenant, but we'll
01:39:42  walk in our new covenant and use our new name in the
01:39:46  name of Jesus. Amen. Amen. Praise God. Well, if you guys need
01:39:50  prayer, we got a prayer team up here. Go in the power
01:39:54  and authority in the name of Jesus. You're dismissed. God bless you.
01:39:59  [singing] [music]
01:40:04  [singing] >> Darkness can't [music] deny the resurrection and [singing] the life. Jesus.
01:40:13  Jesus. [music] Your name can save. Your name can heal. Your name
01:40:19  [music and singing] can make the stor. You never fail. You never will.
01:40:26  Jesus, Jesus, [music] the bread of life [singing] broken for us.
01:40:33  The wounded and the worthy [music] one. The first, [singing] the last,
01:40:39  and still to come. Jesus. Jesus. [singing] The king who overwhelmed
01:40:47  [music] the crane. The Lord who will forever. [singing] The name above
01:40:54  all other [music] names. Jesus.
01:40:59  Jesus be [singing] the name. [music] Jesus be the name.
01:41:07  Jesus [music] be the [singing] name that gets all the glory.
01:41:14  [music] Jesus be [singing] the name.
01:41:18  Jesus be the [music] name.
01:41:22  Jesus [singing] be the name that gets all the glory. [music]
01:41:29  Jesus be the name.
01:41:33  Jesus be the name. [music and singing] Jesus be the name that gets
01:41:40  all the glor.
01:41:44  Jesus be the [music] name.
01:41:48  Jesus be the name.
01:41:52  Jesus be the name that gets [music and singing] all the glory.
01:42:01  [singing]
01:42:04  Oh
01:42:08  [singing] [music] Jesus.
01:42:16  [singing] Oh
01:42:23  [singing]
01:42:26  Jesus.
01:42:33  Oh we thank you Lord.
01:42:39  [singing]
01:42:41  >> We love your name. >> Oh we bless we bless your name.
01:42:51  In the name of Jesus.
```

### 5c. Transcript excerpt — prophetic/ministry language matches

_keyword regex: prophesy/prophetic, word from the Lord, healing, lay hands, tongues, fire, presence, altar, come forward, receive, impartation, deliverance_

```
00:10:57  It's like a fire that [music] shut up in my bones. It's
00:12:22  [music] gra. Let it out. Let it out. It's like a fire
00:25:30  Tap into the presence of God.
00:25:36  >> We thank you, Lord. We acknowledge your presence today. We say yes
00:28:45  can we be healed? Because he loves us. How can we prosper?
00:29:52  love of God. See, that's the healing isn't about works. It's not
00:35:09  [music] in Jesus' name. Amen. Amen. Well, as we prepared to receive
00:36:15  the prophet says things that are not good for you. So he
00:41:31  you ready to receive from the word today? >> Did you come expecting
00:45:58  are waiting on God to heal them? How many Christians do you
01:05:07  you. You got God's spirit. And not only did you receive the
01:07:54  You receive the grace of God. And you and I have been
01:08:43  in my name. In my name, they will speak with new tongues.
01:11:10  out demons in these names. You can speak with tongues. If they
01:13:40  them. >> Oh, I love that. They will lay hands on the sick.
01:13:45  Who's going to lay hands on the sick? >> The covenant man. >> The
01:13:51  covenant woman will lay hands on. We're talking about a covenant man.
01:29:23  [music] Jesus. Your name can save. Your name can heal. Your name
01:40:13  Jesus. [music] Your name can save. Your name can heal. Your name
```


---

## Movement Church (Celina, TX) — Covenant Living - Freedom from Sin (V2KhD7yrmTM)

### 1. Manifest
```json
{
  "church": "Movement Church (Celina, TX)",
  "video_id": "V2KhD7yrmTM",
  "url": "https://www.youtube.com/watch?v=V2KhD7yrmTM",
  "title": "Covenant Living - Freedom from Sin",
  "upload_date": "20260705",
  "duration_seconds": 6063,
  "whisper_model_used": "none \u2014 YouTube 'en-orig' auto-captions (ASR) substituted; Whisper impossible (media download blocked in sandbox, see PIPELINE_REPORT.md)",
  "notes": "replacement for dCWJhrpKUrc (Jul 20 service has no captions available). replacement for dCWJhrpKUrc (Jul 20 service has no captions available)"
}
```

### 2. Segments
```json
{
  "segments": [
    {
      "start": "00:00:00",
      "end": "00:04:41",
      "label": "other",
      "confidence": "high",
      "note": "pre-service countdown"
    },
    {
      "start": "00:04:41",
      "end": "00:28:50",
      "label": "worship",
      "confidence": "high"
    },
    {
      "start": "00:28:50",
      "end": "00:39:30",
      "label": "other",
      "confidence": "low",
      "note": "short exhortation on Christ's intercession; offering lead-in"
    },
    {
      "start": "00:39:30",
      "end": "00:46:00",
      "label": "announcements",
      "confidence": "medium",
      "note": "giving instructions, kids resources, social media promo"
    },
    {
      "start": "00:46:00",
      "end": "01:40:00",
      "label": "message",
      "confidence": "high",
      "note": "Covenant Living - Freedom from Sin"
    },
    {
      "start": "01:40:00",
      "end": "01:41:03",
      "label": "ministry_time",
      "confidence": "low",
      "note": "closing prayer / ministry moment; stream ends mid-prayer"
    }
  ],
  "worship_minutes": 24.1,
  "message_minutes": 54.0,
  "ministry_minutes": 1.1,
  "worship_to_total_ratio": 0.239
}
```

### 3. Speech density (worship + ministry buckets only; 5-min buckets, ASR word counts)
```
00:00–05:00 | 48 words
05:00–10:00 | 376 words
10:00–15:00 | 343 words
15:00–20:00 | 348 words
20:00–25:00 | 260 words
25:00–30:00 | 507 words
1:40:00–1:41:03 | 177 words
```

### 4. Contact sheets (timestamps in tiles are true video time)
```
grid_baseline_01.jpg
grid_baseline_02.jpg
grid_baseline_03.jpg
grid_baseline_04.jpg
grid_baseline_05.jpg
grid_baseline_06.jpg
grid_baseline_07.jpg
grid_dense_ministry_01.jpg
grid_dense_worship_tail_01.jpg
grid_dense_worship_tail_02.jpg
grid_dense_worship_tail_03.jpg
grid_dense_worship_tail_04.jpg
grid_dense_worship_tail_05.jpg
grid_dense_worship_tail_06.jpg
```

### 5a. Transcript excerpt — final 10 min of worship

```
00:18:53  a faithful God. [music] Oh, we worship you, Lord.
00:19:03  We bless [music and singing] your name.
00:19:08  And I'm going to [singing] hit it [music]
00:19:15  with the last name.
00:19:20  [music]
00:19:23  All [singing] the saints and angels [music] they bow
00:19:31  [singing] before your [music] throne.
00:19:37  >> [singing] >> All the elders [music] cast their crowns before [singing] the lamb
00:19:46  of God [music] and [singing] sing all the saints. All [music] the
00:19:53  saints and [singing] angels [music] that bow before [singing]
00:20:01  your throne.
00:20:05  >> [singing and music] >> All the elders cast their crowns [singing] before the lamb
00:20:14  of God and sing. [music] You are worthy [singing] of it all.
00:20:23  Lord, [music and singing] you're worthy of it all.
00:20:31  For [singing and music] from you are all things and to you are all
00:20:37  you deserve. >> You deserve the [music and singing] glory.
00:20:43  All the saints and angels
00:20:47  we sing [music and singing] all the saint and angels
00:20:54  they bow [singing and music] before your throne. Oh,
00:21:02  all [singing] the [music] elders cast their crowns before the lamb
00:21:09  [music] of God and [singing] sing. Lord, you're worthy [music] of it
00:21:15  all. He's worthy. Yes, he is, Lord. [music] You are worthy [singing]
00:21:22  of it all.
00:21:25  Yes, you are. [music] [singing] from you are
00:21:32  [singing] you [music] deserve glory
00:21:40  [singing] [music] you
00:21:48  [singing] see [music]
00:21:54  [singing]
00:21:57  you Heat. Heat. Heat. [music]
00:22:00  [singing]
00:22:03  [music]
00:22:07  Yeah. Heat. [music] [singing]
00:22:16  [music and singing]
00:22:20  Heat. [music]
00:22:25  Heat. [music]
00:22:33  [singing] [music]
00:22:36  you
00:22:39  are [music] so clear right now. We lift our hands, we lift
00:22:43  our voices, and we worship you, Jesus. [music] Oh, there's a night
00:22:47  like you, Lord. There's a man like you, Lord.
00:22:52  [music and singing]
00:22:57  Oh, we [music and singing] bless your name. We bless your name. Oh, [music]
00:23:04  [singing]
00:23:08  and we sing day and [music and singing] night, night and day, their worship
00:23:13  for us. [music] Day and night, [singing] night and day, their worship.
00:23:23  Day and night. [music] Sing it out. We sing day and night.
00:23:30  Heat. Heat. [music and singing]
00:23:36  [singing]
00:23:40  Heat. [music] Heat. [singing]
00:23:47  [music and singing]
00:23:52  Yeah.
00:23:55  Heat. [music]
00:24:01  [music and singing]
00:24:06  [music] [singing] Oh, [music] you
00:24:17  [singing]
00:24:21  [music] [singing]
00:24:31  [music]
00:24:36  [music] Heat. [singing]
00:24:40  Heat.
00:24:44  [music and singing]
00:24:50  Yeah. [music and singing] Heat.
00:24:58  [music] [singing]
00:25:03  Yeah. [music] Heat.
00:25:10  [music]
00:25:15  [music] Oh,
00:25:20  [singing]
00:25:24  [music]
00:25:29  [music] Jesus.
00:25:35  [music]
00:25:38  I
00:25:43  [music] exalt [singing] thee. Exalt the Lord. You are highly [music] exalt.
00:25:52  [singing]
00:25:55  >> I exalt. >> Come on. Let's lift that up this [music] morning. Lord,
00:26:00  [singing] >> I exalt thee. Oh. [music]
00:26:09  >> Oh, [singing] we your name. We exalt you Jesus name. [music]
00:26:16  >> I [singing] exalt thee. >> Oh exalt you Jesus.
00:26:23  >> I [singing] exalt [music] thee >> over everything. Lord
00:26:30  I [singing] exalt thee. [music] >> Oh [singing]
00:26:38  [music] cuz you're worthy of it all. Lord, you're [music and singing] worthy of
00:26:45  it all. We tell him this morning, you're worthy. You're worthy of
00:26:52  it all. [music and singing]
00:26:58  >> For from [music and singing] you are all things and to you are all
00:27:03  things. >> You deserve >> You deserve the glory. [music and singing] You're worthy of it
00:27:10  all. Lord, >> you are worthy [singing] of [music] it all.
00:27:17  >> So worthy, Jes. >> You are worthy of it all. [music] >> So worthy
00:27:23  [singing] of our praise. For from you are all things. [singing] And
00:27:30  to [music] you, >> from you, far from you [singing] are all things.
00:27:37  And [music] to you are all [singing] for from you are all
00:27:42  [music] things and to you are all things. You [music and singing] deserve the
00:27:49  glory.
00:27:53  [singing] [music]
00:27:58  [singing]
00:28:02  [music]
00:28:05  We [singing] [music] bless your name. We bless.
00:28:13  >> We bless your [singing] name. We bless.
00:28:17  [music] >> Oh, we worship you, Jesus. [singing]
00:28:24  [music] >> Lord, we praise you. >> We praise you. >> Worthy of it all.
00:28:31  All glory is yours, Lord. [music] You are so worthy. Thank you
00:28:35  Lord every day for this amazing country [music] you put us in.
00:28:39  Thank you Lord for giving us a place where we can freely
00:28:43  worship you, where we can put you in your rightful place above
00:28:47  all things because you are the only [music] one one worthy to
00:28:50  be put above all things. Thank you God. You know when I
```

### 5b. Transcript excerpt — ministry time (entirety)

```
01:40:04  our flaws. But Lord we can lean into our covenant and our
01:40:08  covenant promises and declare say what you say about us. We can
01:40:13  trust what you say and we can lean on your word and
01:40:17  stand on our covenant promises. Thank you, Lord, for setting us free
01:40:23  from sin. Thank you, Lord, that we don't have to be condemned.
01:40:28  Thank you, Lord, that we don't have to live that way any
01:40:30  longer in the name of Jesus. Amen. Amen. Thank you, Lord. If
01:40:36  you need prayer today, I want you to come forward after the
01:40:38  service. If you've been tormented by this, I I feel like today
01:40:42  there's been people that have been just so tormented by this sin
01:40:45  issue. It's really bothered you. And I believe today the Lord is
01:40:49  opening your eyes and setting you free. Amen. Amen. If you need
01:40:53  prayer, come forward after the service. We love you guys. Have a
01:40:56  great week this week. God bless you. And we'll see you next
01:40:58  Sunday.
```

### 5c. Transcript excerpt — prophetic/ministry language matches

_keyword regex: prophesy/prophetic, word from the Lord, healing, lay hands, tongues, fire, presence, altar, come forward, receive, impartation, deliverance_

```
01:03:12  to the altar that is before the Lord and make atonement for
01:03:22  were sacrificed. And put it on the horns of the altar all
01:40:36  you need prayer today, I want you to come forward after the
01:40:53  prayer, come forward after the service. We love you guys. Have a
```


---

## Movement Church (Celina, TX) — Healing Night - May 2026 (S5hmFAr6iUs)

### 1. Manifest
```json
{
  "church": "Movement Church (Celina, TX)",
  "video_id": "S5hmFAr6iUs",
  "url": "https://www.youtube.com/watch?v=S5hmFAr6iUs",
  "title": "Healing Night - May 2026",
  "upload_date": "20260507",
  "duration_seconds": 6397,
  "whisper_model_used": "none \u2014 YouTube 'en-orig' auto-captions (ASR) substituted; Whisper impossible (media download blocked in sandbox, see PIPELINE_REPORT.md)",
  "notes": "metadata via yt-dlp web_embedded client (datacenter IP bot-check workaround); livestream release 2026-05-06T23:55:19Z"
}
```

### 2. Segments
```json
{
  "segments": [
    {
      "start": "00:00:00",
      "end": "00:29:30",
      "label": "worship",
      "confidence": "high",
      "note": "service opens directly in worship"
    },
    {
      "start": "00:29:30",
      "end": "01:01:30",
      "label": "message",
      "confidence": "high",
      "note": "teaching on the anointing and healing"
    },
    {
      "start": "01:01:30",
      "end": "01:45:37",
      "label": "ministry_time",
      "confidence": "high",
      "note": "healing ministry: laying on of hands, prayers over conditions, reports of pain leaving"
    },
    {
      "start": "01:45:37",
      "end": "01:46:37",
      "label": "other",
      "confidence": "high",
      "note": "birthday blessing, dismissal, closing chorus"
    }
  ],
  "worship_minutes": 29.5,
  "message_minutes": 32.0,
  "ministry_minutes": 44.1,
  "worship_to_total_ratio": 0.277
}
```

### 3. Speech density (worship + ministry buckets only; 5-min buckets, ASR word counts)
```
00:00–05:00 | 83 words
05:00–10:00 | 525 words
10:00–15:00 | 487 words
15:00–20:00 | 485 words
20:00–25:00 | 351 words
25:00–30:00 | 390 words
1:00:00–1:05:00 | 715 words
1:05:00–1:10:00 | 806 words
1:10:00–1:15:00 | 631 words
1:15:00–1:20:00 | 776 words
1:20:00–1:25:00 | 688 words
1:25:00–1:30:00 | 676 words
1:30:00–1:35:00 | 700 words
1:35:00–1:40:00 | 788 words
1:40:00–1:45:00 | 649 words
1:45:00–1:46:37 | 149 words
```

### 4. Contact sheets (timestamps in tiles are true video time)
```
grid_baseline_01.jpg
grid_baseline_02.jpg
grid_baseline_03.jpg
grid_baseline_04.jpg
grid_baseline_05.jpg
grid_baseline_06.jpg
grid_baseline_07.jpg
grid_dense_ministry_01.jpg
grid_dense_ministry_02.jpg
grid_dense_ministry_03.jpg
grid_dense_ministry_04.jpg
grid_dense_ministry_05.jpg
grid_dense_ministry_06.jpg
grid_dense_ministry_07.jpg
grid_dense_ministry_08.jpg
grid_dense_ministry_09.jpg
grid_dense_ministry_10.jpg
grid_dense_ministry_11.jpg
grid_dense_ministry_12.jpg
grid_dense_ministry_13.jpg
grid_dense_ministry_14.jpg
grid_dense_ministry_15.jpg
grid_dense_ministry_16.jpg
grid_dense_ministry_17.jpg
grid_dense_worship_tail_01.jpg
grid_dense_worship_tail_02.jpg
grid_dense_worship_tail_03.jpg
grid_dense_worship_tail_04.jpg
grid_dense_worship_tail_05.jpg
grid_dense_worship_tail_06.jpg
```

### 5a. Transcript excerpt — final 10 min of worship

```
00:19:35  the Lord most [singing] high. All praise to the one who saves
00:19:42  my life. [music] All praise to Jesus [singing] Christ, high king of
00:19:49  heaven, my king forever.
00:19:54  >> Come on, let's [music] lift our hands [singing] and worship the Lord.
00:20:02  You are [singing] my king. [music]
00:20:07  You are my king, [music and singing] Lord.
00:20:13  Oh, [singing] we bless [music] your name. Oh, we give you praise.
00:20:20  You are the same each and every [music and singing] day. So, we bless
00:20:27  your name, Lord. We give you praise. You are the same
00:20:35  every day.
00:20:38  We worship you, Jesus. We thank you, Father. We bless your name,
00:20:45  Jesus. You're such a good and a faithful God.
00:20:49  We welcome you in this place tonight.
00:20:56  [music]
00:21:05  >> [singing] >> I simple melodies [singing] of sacrifice.
00:21:15  Open hands and open [music and singing] hearts. You're the only one I want.
00:21:23  Treasure my [singing] delight.
00:21:30  like
00:21:34  Holy [music] Spirit [singing] fall like gra Holy
00:21:41  [music and singing] Spirit have your way. Let [singing] your
00:21:48  glory fall down. Let your glory fall [music] down.
00:21:56  thing I ask, I seek so [music and singing] much more than anything to
00:22:03  dwell within your house for all [music and singing] my days.
00:22:09  Lord, knowing you is [music and singing] everything. So I let go of lesser
00:22:15  things. You alone are [singing] worthy [music] of my praise.
00:22:23  So stir in [singing] me a passion for your name.
00:22:30  All [singing] I pray Holy [music] Spirit fall
00:22:39  I pray. Holy [music and singing] Spirit have your
00:22:47  way. Let your glory [singing and music] fall down. Let your glory
00:22:54  fall down.
00:22:58  Fall. [singing] [music]
00:23:03  Holy Spirit. Fall. [music and singing]
00:23:10  Holy [music and singing] Spirit. Have your way. Let
00:23:17  [singing] your glory [music] fall down. Let your glory [singing] fall [music]
00:23:22  down.
00:23:30  Have your way. Have your [music] way. [singing]
00:23:38  May I never lose the wonder of your [singing] presence. [music] May
00:23:45  I always stand in awe of who you are.
00:23:51  Oh, the beauty and [music] the gift of your friendship
00:23:58  is unlike anything I've ever known. [music and singing] May I never May I
00:24:06  never lose the water [singing] of the [music] resence. We always
00:24:14  stand and [singing] above who you are. [music]
00:24:19  Oh, the [singing] beauty and the gift [music] of the over
00:24:27  like [music] anything I've ever known so far. [music and singing]
00:24:36  Oh, Holy Spirit. Holy [music] Spirit fall [singing]
00:24:45  away. Holy Spirit [music] of you. [singing]
00:24:52  Let your [music] glory fall down. Let your [singing] glory fall.
00:24:59  [music] Oh my. [singing]
00:25:06  Holy Spirit [music] pour
00:25:12  come and have your way. Have you
00:25:19  [music and singing] let your glory forever
00:25:26  [music]
00:25:29  lose the wonder [music] of [singing] your words?
00:25:36  [singing]
00:25:39  All the beautiful [music]
00:25:44  gift [music and singing] your gra
00:25:54  [music]
00:25:58  [music] [singing] your presence I always stand of who you
00:26:09  of the beauty and the [music] gift of [singing] your presence
00:26:16  unlike anything [music] I've ever known.
00:26:23  All [music and singing] I pray, Holy [singing] Spirit,
00:26:32  I pray, Holy [singing] Spirit, [music] have your
00:26:40  way. Let [singing] your glory [music] fall down. Let your glory
00:26:47  fall down. Let it fall. >> [music and singing]
00:26:55  >> Let it fall. [singing]
00:27:01  Come on, let's lift our hands and we [music] press into [singing]
00:27:05  his presence. Oh, we turn our attention to you, Jesus. [music] May
00:27:11  we never forget. [singing] May we never forget.
00:27:18  You are the one true living God. [music]
00:27:27  Oh, we bless your name. [music]
00:27:34  We bless your name. >> Praise your name. >> We bless [singing] your name.
00:27:41  We bless your name. [music]
00:27:50  >> [singing]
00:27:54  >> like rain.
00:27:59  Come on, church. Let's just press in for just another minute. [music]
00:28:02  Just lift your hands, lift your [singing] voices. Oh, we thank you,
00:28:05  Lord.
00:28:09  [singing] >> [music]
00:28:14  [singing] [music] >> We praise you.
00:28:21  [singing]
00:28:24  [music] Oh, we bless your name. We give
00:28:31  you praise. [singing and music]
00:28:41  We thank you, Father. We thank you, Father. >> Thank you, Jesus. >> We
00:28:48  thank you, Jes. >> Oh, let's just lift up our hands right now
00:28:51  and thank him. Let's just thank him for being a good God.
00:28:55  Thank him for his glory. Thank him for his goodness. Thank him
00:29:00  for his power. Thank him for the fact that you're here tonight.
00:29:05  [music] >> That he's kept you your entire life. >> Thank you, Lord,
00:29:13  >> that we live in this amazing country where we can worship you
00:29:18  freely. Oh, thank you, [music] Lord. Thank you, Lord. Thank you, Lord.
00:29:27  You know, there's just nothing like being in the presence of God.
```

### 5b. Transcript excerpt — ministry time (entirety)

```
01:01:30  body, if you're having any kind of physical problems, mental problems, thank
01:01:36  you, Lord.
01:01:42  Thank you, Lord, for the anointing. Thank you, Lord, for the anointing.
01:01:49  Let's just be praying right now, listening to the Holy Spirit. Let's
01:01:52  listen to his voice.
01:01:57  Thank you, Lord. Thank you, Jesus.
01:02:07  Thank you, Lord. Thank you, Lord.
01:02:15  What can we pray with you?
01:02:19  Ringing.
01:02:26  Yeah. Acting up.
01:02:31  Well, the devil's getting on your nerves. That's what I just heard.
01:02:34  So, we're going to get the devil off your nerves in the
01:02:37  name of Jesus and the anointing that's on our life. We declare
01:02:41  right now, nerves, you function properly. Devil, you get off her nerves
01:02:45  right now in Jesus name. Nerves, you function properly in the name
01:02:50  of Jesus. Will not have this. She's a child of the king.
01:02:53  We pray and agree right now. the prayer of faith, believing, trusting
01:02:59  you, Lord, as the healer. And that anointing right now is flowing
01:03:04  into her body, healing what's been broken, uh, putting together, what's been
01:03:09  disconnected. Thank you, Lord, that she does not have to have this
01:03:13  the rest of her life. I don't care what others have said.
01:03:17  The answer is no. God says, "No, you don't have to have
01:03:21  this. The world says you do." The world says, "Oh, it's just
01:03:24  a part of Bell's policy. Oh, it's just a part of this."
01:03:27  But you've been redeemed from the curse of the law. That doesn't
01:03:31  apply to you. Thank you, Lord, for healing right now in the
01:03:35  name of Jesus. Every nerve, every nerve functioning properly in the name
01:03:42  of Jesus. Thank you, Father. Yes, ma'am.
01:03:48  Oh, put your hand right there on her chest. In the name
01:03:51  of Jesus, we rebuke that crud. We pray the prayer of faith
01:03:55  over her right now. Healing, wholeness over her lungs, clear lungs in
01:04:00  the name of Jesus Christ of Nazareth. Thank you, Lord, for that
01:04:04  anointing right now flowing into her body. The spirit of the Lord
01:04:09  is upon us. We are anointed for this purpose to lay hands
01:04:14  on the sick. And the sick, you have no choice. You have
01:04:17  to recover in the name of Jesus. Lungs, you have to be
01:04:21  clear right now in Jesus name. Oh, just take a deep breath.
01:04:25  Take a deep breath. Thank you, Lord, for clear lungs in the
01:04:28  name of Jesus. Thank you, Lord. Thank you, Lord. Clear lungs in
01:04:34  the name of I'm glad you came forward because the Lord told
01:04:36  me to pray for you tonight. You weren't coming forward. I was
01:04:39  calling you out, girl. Thank you, Lord.
01:04:49  Yes. Yes. Thank you, Lord. Thank you, Lord. Lay your hands on
01:04:53  her back. Father, in the name of Jesus, we come into agreement
01:04:59  right now. Thank you, Lord, for the anointing. Thank you, Lord, for
01:05:04  the anointing. Oh, the spirit of the Lord is upon us. We
01:05:08  are anointed. You got a bunch of anointed hands laying on you
01:05:12  right now. Back, you line up in Jesus name. Body, you recover
01:05:16  in Jesus name. Oh, I I just see uh the enemy has
01:05:20  just been after you when your physical body and it and it
01:05:24  just seems like when one thing seems to come and go, then
01:05:27  something else is popping up. And and I and that the Lord
01:05:30  wants you to know that that is the enemy trying to distract
01:05:33  you, trying to bring you down. And it's time to take a
01:05:37  stand right now. And tonight you're taking that stand. And by faith
01:05:42  receive all. I said all. I said all of the anointing that's
01:05:46  needed to heal every aspect, every every symptom in the name of
01:05:52  Jesus. I rebuke that in her body in Jesus name. Back you
01:05:56  function properly. Pain you leave in the name of Jesus. From the
01:06:00  top of her head to the soles of her feet. And devil
01:06:04  you take your hand off of God's property [music] right now. You
01:06:08  take your hands off of her. She's a child of the most
01:06:11  high God. She's the temple of the Holy Spirit. And the same
01:06:16  spirit in her is the spirit that kicks your tail all over
01:06:20  this earth. That spirit is rising up on the inside of her.
01:06:25  Oh, thank you, Lord, that she becomes a dangerous person for the
01:06:29  enemy to try to attack. A dangerous person that the enemy says,
01:06:33  "You better leave." No, leave that one alone cuz she's dangerous. Oh,
01:06:38  she's going to she's going to come after us. She's going to
01:06:41  be saying things about us. How she's been healed, how she's been
01:06:45  delivered, how she no longer deals with those things any longer because
01:06:50  by Jesus stripes, she was healed. Thank you, Lord, for it. Thank
01:06:56  you for that anointing right now. It's flowing in your body right
01:07:00  now. I can feel my fingers tingling right now. The anointing is
01:07:04  coming in. Oh, it's healing everything. Everything that's out of alignment in
01:07:09  her body. Things on the inside. Oh, things on the inside are
01:07:13  being healed right now in the name of Jesus.
01:07:19  You don't have to be guilty about anything. You don't have to
01:07:22  say, "Oh, I ate this, so I going to have to have
01:07:25  that." Absolutely not. You don't have to have any of that junk.
01:07:30  You don't have to [music] accept any of that curse because you
01:07:33  are redeemed from it in Jesus name. Thank you father. Thank you
01:07:38  Lord. >> Yes. >> Yes. Yes.
01:07:46  Yeah.
01:07:51  >> Thank you Lord.
01:07:56  Well, you know, there was a time when Jesus healed people that
01:08:00  weren't present. Actually, there was multiple times where he did that with
01:08:04  a centurion servant. He said, "I'll come heal your servant." And what
01:08:07  did what did the centurion say? He said, "You don't have to
01:08:12  come. Just speak the word. Just speak the word." We're going to
01:08:16  speak some words tonight. We're going to speak some words. Thank you
01:08:19  for standing in. Father, in the name of Jesus, we speak to
01:08:22  that inflammation in Caleb's mouth right now in the name of Jesus.
01:08:26  Thank you, Lord. He does not have [music] to have this. Oh,
01:08:30  I see this as a sign in his life. Oh, thank you,
01:08:33  Lord, that right now that healing power is going into his body,
01:08:38  mouth, you be restored in the name of Jesus. Thank you, Lord.
01:08:41  And there'll be no other explanation. Oh, no. the the the way
01:08:46  it was done, the way it happened, there'll be no one [music]
01:08:49  to get credit but God almighty. Thank you, Lord. Thank you, Lord.
01:08:54  We speak to that mouth right now in Jesus name. Be healed
01:08:58  in Jesus name. Oh, thank you, Father.
01:09:05  And he'll and I and I just see this. He'll say he'll
01:09:07  give glory to God without even realizing he did it. He'll be
01:09:10  like, "Whoa, I didn't know I said that." But he'll give glory
01:09:13  to God. It'll just come slipping out of his mouth. Just come
01:09:16  right out of his spirit. He'll give glory to God for it.
01:09:20  Thank you, Lord. He's healed by Jesus stripes. >> Thank you, Lord. >> Thank
01:09:26  you, Jesus, for that anointing flowing in his mouth right now in
01:09:30  Jesus name. Restoring in Jesus name. Thank you, Lord. And here's something
01:09:34  else I heard the Lord say. You know, everybody that Jesus healed
01:09:38  in the in all of his ministry, you know, they weren't perfect
01:09:42  people. None of them were even born again.
01:09:46  Let me tell you something. Nothing disqualifies you. Nothing.
01:09:53  Nothing disqualifies. Thank you, Lord. Praise you, Father. Thank you, Lord.
01:10:02  Pain gone. Pain from that kidney stone. Yeah. Yep. Father, in the
01:10:09  name of Jesus, as we lay hands on her, we do exactly
01:10:13  what you said. The anointing oil right now is flowing in her
01:10:18  body. Thank you, Lord. Thank you, Lord. Pain you leave right now
01:10:24  in Jesus name. Oh, kidney stone, you're rebuked in her body. Anything
01:10:30  remaining, anything trying to form, I rebuke it in the name of
01:10:34  Jesus. We come into agreement with Crystal right now. I thank you,
01:10:38  Lord, that that anointing is flowing in her body right now. Healing
01:10:43  what has been damaged. Oh, restoring what's been damaged in the name
01:10:48  of Jesus. Oh, this is nothing but a silly little distraction. Just
01:10:53  a silly little distraction. And in the name of Jesus, we call
01:10:58  this finished, done, over in the name of Jesus. Thank you, Lord,
01:11:05  for that anointing. Thank you right now. Right now, in the name
01:11:10  of Jesus. The spirit of the Lord is upon you. He's anointed
01:11:15  you. And that anointing removes burdens. This is a burden. This is
01:11:20  a burden. I rebuke that in Jesus name. I rebuke [music] that
01:11:25  burden. Tell it to leave and anointing. You do what you do.
01:11:30  Set her free in Jesus name. Thank you, Lord. Yes, ma'am.
01:12:04  Let's pray for you. Okay, we lay hands on you and pray
01:12:07  for you. Thank you, Father. Oh, for the childlike faith. Oh, you
01:12:13  said in your word, you said, "Oh, keep them away. Keep them
01:12:17  away." And no, Jesus, you said, "Bring them in. Bring them in."
01:12:22  Thank you Lord for that healing power. Thank you Lord for removing
01:12:27  that itch in the name of Jesus. Restoring her skin, restoring her
01:12:31  body. Oh, I thank you Lord for that anointing right now in
01:12:36  the name of Jesus. Even at her age, she's experiencing it. This
01:12:41  is the normal. This is normal. This is just the norm. Thank
01:12:45  you, Father, for that anointing removing this itch in Jesus name. And
01:12:51  we just speak wholeness over her body in the name of Jesus.
01:12:54  This will not be a lingering thing. This thing ends [music] tonight
01:12:58  in the name of Jesus. Thank you Lord for the anointing. The
01:13:03  elders have laid hands on anointed her with the oil of the
01:13:07  Holy Spirit and body. You recover in Jesus name. We speak to
01:13:12  it. Say recover in the name of Jesus. Amen. Amen. Thank you
01:13:17  Lord. Praise you father.
01:13:22  busted your hand.
01:13:25  >> Oh man. >> Yes. >> Yes. >> Father, in the
01:13:32  name of Jesus, we thank you for that anointing. You said you
01:13:39  said that Josh could come forward tonight and call on prayer. The
01:13:45  prayer of faith you said will save the sick. We are to
01:13:48  anoint him with oil right now. The oil is flowing in his
01:13:51  arm right now in his hand. Oh, restoring what's been messed up.
01:13:56  Oh, the nerves and the tendons. Oh, anything out of alignment. Anything
01:14:00  that's off, anything that's broken, we speak restoration over it right now
01:14:04  [music] in the name of Jesus. Thank you for the anointing. Thank
01:14:10  you for that anointing flowing in his hand right now. The power
01:14:13  is flowing right now. Oh, it's flowing right now in the name
01:14:18  of Jesus. things that he couldn't do now he'll be able to
01:14:21  do. Thank you Lord. We call his hand restored in the name
01:14:25  of Jesus. >> Restoration, wholeness, >> healing in the name.
01:14:33  >> In the name of Jesus. Thank you Lord. Thank you Lord. >> Were
01:14:37  you able to bend it before?
01:14:41  >> Praise God. Thank you Lord. >> Well that seems to be working. Praise
01:14:48  God. Thank you, Lord. >> Thank you, Jesus. >> Thank you, Lord. Praise. Let's
01:14:55  just praise him for a minute. Let's just praise him for a
01:14:58  minute. Thank you, Lord. Thank you, Lord. Jesus, for being our healer.
01:15:04  Thank you, Lord. Pastor Chris is not the healer. Jesus is the
01:15:08  healer. But Jesus has anointed us. He's empowered us to lay hands
01:15:16  on broken hands, broken bodies, sickness, and disease. And sickness,
01:15:23  disease, and broken hands have to bow their knee to the anointing
01:15:28  of the Holy One of Israel, Jesus Christ, the anointed one. Thank
01:15:34  you, Father. Thank you, Jesus. I'm stirred up. Thank you, Lord. Praise
01:15:39  God. Did you need prayer?
01:15:43  Oh, his tongue. Yeah, he told me earlier he bit his tongue
01:15:46  earlier. [music] Father, in the name of Jesus. Oh, thank you, Father,
01:15:50  for restoring his tongue. Oh, that pain that Oh, we we've all
01:15:54  experienced it. Every single one of us have experienced pain. We we
01:15:58  bite our tongue. And so, I thank you, Lord, for restoration in
01:16:01  his tongue in Jesus name. I rebuke the pain right now in
01:16:04  the name of Jesus. The spirit of the Lord is upon us.
01:16:08  You have anointed us and that anointing is flowing in his body
01:16:12  right now in the name of Jesus. We thank you for it.
01:16:16  We praise you for it in Jesus name. Amen. Amen. Thank you
01:16:20  Lord. How's your tongue feeling?
01:16:25  You feeling better too? Praise God. Thank you Lord. >> Yes ma'am.
01:16:35  >> Your leg. Which leg is it? Well, let me just get down
01:16:38  here and we're just going to lay hands on your leg. And
01:16:41  when we lay hands on your leg, the power of God is
01:16:44  [music] going to come into your leg. Okay? Father, in the name
01:16:47  of Jesus, we rebuke this pain in Jesus name. Thank you, Lord.
01:16:52  Her leg is restored. Whatever the source of this pain is, we
01:16:56  don't even have to know what it is. It could just be
01:16:58  a bruise. It just could be something else. Doesn't matter. Leg be
01:17:02  restored in the name of Jesus. The spirit of the Lord is
01:17:05  upon us. You have anointed us. >> That anointing right now is flowing
01:17:10  in her leg in Jesus name. Restoring and removing the pain. Pain
01:17:16  you be gone in Jesus name. You leave her body in the
01:17:19  name of Jesus. Thank you Lord. Praise you. Now you can run
01:17:23  and jump and play.
01:17:27  Thank you Lord. Praise God. >> His tummy. >> Okay. Well, let's pray for
01:17:34  his tummy. Father, in the name of Jesus, we do exactly what
01:17:38  you said in your word. You said the spirit of the Lord
01:17:41  is upon us. You've anointed us. Thank you, Lord, for that anointing.
01:17:46  Thank you, Lord. That anointing right now is healing his tummy in
01:17:49  Jesus name. Tummy, you line up. You function properly in the name
01:17:54  of Jesus. That anointing right now is healing his stomach. Stomach ache,
01:17:58  you leave his body, you don't belong there. You leave. He's a
01:18:02  child of the most high God. You have no right to him
01:18:06  in the name of Jesus. And we rebuke this attack on his
01:18:10  body [music] in Jesus name. Amen. Amen. Thank you Lord. Praise God.
01:18:15  Thank you Lord. Thank you Lord. Who wants to stand in for
01:18:19  Jada? Kim, you look like Jada. You're here in front of me.
01:18:27  Jada was having some health issues. Jamie and Jasmine's little girl's having
01:18:31  some health issues this morning. And so she had to go uh
01:18:35  to the to the ER actually this morning. And so uh I
01:18:38  just want you to stand in for her because you know what?
01:18:41  The anointing has no distance limitations. There are no distance in the
01:18:47  spirit. So, Father, in the name of Jesus, as I lay my
01:18:52  head right now on Tim's head, thank you, Lord, that that anointing
01:18:56  is flowing in Jada's body in the name of Jesus. Oh, we
01:19:01  speak to her brain. >> You align in Jesus name. Things that are
01:19:07  off, you come back into balance in the name of Jesus. We
01:19:11  will not have this. We will not stand for it. We won't
01:19:15  Oh no. Oh no. Well, this is not happening in her body.
01:19:19  Oh, no. The the doctors have said, "Well, that's the way it's
01:19:22  going to be because it's hereditary." But the Lord says it's not.
01:19:28  >> The Lord says it's not hereditary. She's a child of the most
01:19:33  high. And that anointing right now is correcting everything that's out of
01:19:40  alignment in the name of Jesus. Thank you, Lord. Thank you for
01:19:43  the anointing. The spirit of the Lord is upon us. You've anointed
01:19:48  us. Thank you, Lord, for complete and total restoration in the name
01:19:53  of Jesus. Amen. And amen. Thank you, Lord. Praise you, Father. Yes,
01:19:58  ma'am. Yes, Jimmy.
01:20:06  >> Yes.
01:20:09  >> Thank you, Lord. >> Yes. Absolutely. She's standing in for her friend Jimmy
01:20:15  that's got heart issues in the name of Jesus as we lay
01:20:19  hands on Francesca tonight. Oh, thank you Lord that hands are being
01:20:24  laid right now on Jimmy. Oh, thank you Lord. You're the restorer.
01:20:28  The anointing restores. Thank you Lord for restoration in Jimmy's heart in
01:20:34  Jesus name. Thank put your hand right there on on where her
01:20:37  heart is. Thank you Lord for restoration right now in the name
01:20:41  of Jesus heart. We're speaking to you heart, you beat properly in
01:20:46  Jesus name. Heart, you be restored in the name of Jesus Christ
01:20:51  of Nazareth. The anointing is now touching you. The anointing is repairing
01:20:56  you. The anointing is causing you to be properly. You line up
01:21:00  in the name of Jesus. Thank you, Lord, for it. We call
01:21:05  it done in the name of Jesus. >> The spirit of the Lord
01:21:09  is upon us. You have anointed us. to do this to heal
01:21:16  hearts that are not working [music] properly. Broken hearts, but not just
01:21:20  in in emotional broken hearts, but physical hearts that are broken. I
01:21:26  thank you, Lord. His heart is restored. He gets a new heart.
01:21:30  Oh, thank you, Lord. It's like new. And the doctors will even
01:21:32  say, "It's like you got a new heart. It looks like the
01:21:36  old one, but you got a new one." And it's because of
01:21:38  the anointing. Thank you, Lord, for that anointing. restoring. Oh, and everything
01:21:44  that's been damaged because of his heart. Oh, any artery, any vein,
01:21:49  any any uh limb, any other symptoms that he's having, I rebuke
01:21:54  those in the name of Jesus. Thank you for that anointing from
01:21:59  the top of his head to the soles of his feet right
01:22:01  now. Restoring, restoring, restoring what the doctors say cannot be restored that
01:22:08  they say, "Oh, he'll have this problem the rest of his life."
01:22:11  We say no because of the anointing. It's restoring right now in
01:22:17  Jesus name. Thank you Lord for it. Praise you for Thank you
01:22:20  Lord. You you you talk to him. You tell him what we just
01:22:23  prayed tonight. >> Thank you Lord. Praise you father. That anointing is working
01:22:29  in his body in the name of Jesus. Praise you father. Let's
01:22:34  just thank you for a moment. Isn't God good? Let's just thank
01:22:37  him for a moment. Thank you Lord for the anointing. [music]
01:22:44  Let's pray in the spirit because the spirit of the Lord is
01:22:48  upon us. Let's just pray in the spirit.
01:22:57  Let's just sing in the spirit. Sing in the spirit tonight.
01:23:03  Thank you, Lord.
01:23:13  >> [music and singing] >> Let's just keep singing. Just keep singing for a moment.
01:23:18  [music] [singing]
01:23:24  [music]
01:23:28  >> [singing and music]
01:23:33  >> Owen, is it okay if I pray for you? >> Come up. I
01:23:37  want to lay hands on you and pray for you. Thank you,
01:23:40  Lord. >> I just felt impressed to pray for you. I don't know
01:23:44  what I'm praying over, but the spirit knows. Praise the Lord. Thank
01:23:49  you, Lord. Is there something or no? Don't even tell me. Thank
01:23:52  you, Lord. Father, in the name of Jesus, I pray for my
01:23:56  brother right now. Oh, the spirit of the Lord is upon us.
01:24:01  You've anointed us. He's anointed. Thank you for that anointing that's on
01:24:05  his life. Thank you, Father. Thank you, Lord, that he's protected and
01:24:11  he's kept in Jesus name. Oh, thank you, Lord. We rebuke any
01:24:16  attack from the enemy that would try to come after him and
01:24:22  convince him and change his mind about things. No, no, no. The
01:24:28  Lord says no. Thank you, Lord. You're a child of the most
01:24:33  high. You don't have to accept anything less than what God says
01:24:37  you are. What God says you can have. Thank you, Lord. And
01:24:42  I just feel in my spirit that there have been some things
01:24:46  that have been said about you, been spoken either to you or
01:24:50  about you that have kind of put some limits in your life.
01:24:54  And the Lord wanted me to tell you tonight, those limits don't
01:24:58  exist.
01:25:00  Those don't exist. Those limits are self-imposed limits. Thank you, Lord. There
01:25:07  are no limits. From God's perspective, there are no limits to what
01:25:12  you can do. He said you can do all things through Christ,
01:25:17  through the anointing that's on your life, strengthening you, empowering you. You
01:25:21  have value. You have purpose. Thank you, Lord. The enemy has has
01:25:28  tried to kind of work on you a little bit. Say, well,
01:25:31  you know, you're not much of [music] this or not much of
01:25:33  that. And he's really tried to belittle you a little bit. tried
01:25:36  to say, "Well, you're not this, you're not this kind of person."
01:25:39  And and you know, the Lord would say, "Stop listening to that
01:25:42  voice and stop playing the comparison game. He's anointed you in a
01:25:47  unique and special way." We're all unique and special. And don't let
01:25:53  the devil lie to you. Don't let the devil persuade you and
01:25:56  and try to tell you that you're not enough and that you
01:26:00  can't. The Lord says you can. You can what? You can do
01:26:04  all things through Christ strengthening you. Whatever it is he puts on
01:26:08  your heart to do. Whatever it is you stretch forth your hand
01:26:11  to do, the Lord says he'll make you prosper. You step out
01:26:15  in faith, you follow the leading of the Holy Spirit and you
01:26:18  do what he tells you to do and the Lord said I'm
01:26:21  when my hand is in it and you're following me, it'll prosper
01:26:24  and you'll be successful in all that you do. Be bold. Be
01:26:30  courageous in the name of Jesus. Thank you Lord. Thank you Lord
01:26:35  for boldness in Jesus name. Thank you Father. Does that bear witness
01:26:39  with your spirit? Thank you Lord. Praise you father. Thank you Lord.
01:26:43  Let's just pray in the spirit [music] for a minute. It's okay.
01:26:46  It's Wednesday night. We might as well hang out a while. Thank
01:26:49  you Lord. Thank you Lord. [singing]
01:27:03  depression. >> You're suffering from depression tonight. I want you to come forward
01:27:07  right now. [music and singing] >> You're suffering from depression. You've been depressed. Somebody here
01:27:14  has been depressed. You've been suffering from it. It may maybe it's
01:27:18  been a short-term thing. I don't know if it's short or long
01:27:20  term, but you've been suffering from depression. The Lord says healing [music]
01:27:24  night is not just for physical things. Healing not is for everything
01:27:28  that's been hindering you. Thank you, Lord.
01:27:33  Thank you, Lord. Thank you, Lord. I heard the Lord say this.
01:27:40  You may not think it's been depression, but you've had thoughts that
01:27:45  have been belittling, be degrading thoughts, and you've been thinking about bad
01:27:51  things. And like, it's like these bad things have been rehearsing in
01:27:55  your mind. And the Lord said, "That's the seed of depression, anticipation
01:28:01  of evil, and you've been rehearsing these negative things in your mind."
01:28:06  And the Lord said, "Yeah, you don't recognize it's depression. That's why
01:28:10  you're not coming forward." But the Lord said, "The seed is there.
01:28:15  The seed has been planted of depression." And you need to deal
01:28:18  with that seed. You need to deal with it tonight. It needs
01:28:22  to be uprooted in the name of Jesus. Thank you, Lord. Thank
01:28:28  you, Lord. You've had bad thoughts, evil thoughts, just rehearsing over and
01:28:33  over in your mind. Thank you, Lord. Thank you, Jesus. We'll wait
01:28:39  just a minute. >> And I just heard the Lord say that. You
01:28:43  said, "Well, that's not me. I'm not a depressed person." But you've
01:28:46  been having these thoughts.
01:28:50  Those negative thoughts will lead to and grow depression in your mind.
01:28:57  And the Lord wants you free tonight. That's why he had me
01:29:00  say it. That's why you came tonight. Didn't even know you came
01:29:04  for it, but that's why you came to be set free. Thank
01:29:07  you, Jesus.
01:29:14  Thank you Lord. Thank you Lord. Let's just worship him. Let's worship
01:29:19  him.
01:29:27  >> Oh [music and singing] we bless your name. We bless your name.
01:29:33  [music] [singing]
01:29:50  Oh [music and singing] yeah, I'm a man. I'm a
01:30:07  >> Thank you. You know, it ought not be it ought not be
01:30:11  com uncomfortable for us to just worship in his presence. I think
01:30:16  so many times we get in [music] a hurry. We got to
01:30:18  do this or do that. But just spending time in his presence
01:30:23  listening. I want I want you to practice that right now. Just
01:30:26  listen. Listen to what he's saying. You might get answers to questions
01:30:30  you've had your entire life in the next two or three minutes
01:30:34  as we worship. Thank you. That's what I'm doing. I'm listening. I'm
01:30:39  listening for more instructions. >> Thank you, Lord. Just listen. Worship him and
01:30:46  listen in your heart. What is he telling you? What is he
01:30:50  saying?
01:31:07  He may give you a word to [music] share with everybody. Share
01:31:10  it. >> Thank you, Lord. Thank you, Jesus. [singing]
01:31:19  Thank you, Lord. Thank you, Lord. Grab this in the basket. Thank
01:31:24  you, Lord. >> I just had it in my heart that someone's got
01:31:27  a word. Jonathan. >> So, uh, something I saw today bore
01:31:35  witness with my spirit and I believe I should share it here
01:31:39  today. Uh, there was a man that Jesus approached and he asked
01:31:44  him a very simple question. He said, "Do you want to be
01:31:47  healed?" >> Do you want to be healed? And it it's simple in
01:31:54  theory, but the man had been there for years sitting there waiting
01:32:00  for the stirring of the waters. And many of you guys here
01:32:03  tonight, I believe the Lord is asking that question. Do you want
01:32:07  to be healed? Do you want to follow me for the rest
01:32:12  of your life? Do you want to serve me? Do you want
01:32:14  to fulfill the purpose that I have for you? >> Why is he
01:32:19  asking you that? Because is going to require you to get up
01:32:24  and move from where you are to where God is calling you
01:32:28  to be. Yes, that is the vision and the purpose of this
01:32:34  church. How many of you guys would would say tonight that you
01:32:40  are in a position where God is asking you to do something
01:32:45  that may be uncomfortable that that may be something that requires you
01:32:50  to make a change that you're not sure about yet. Remember the
01:32:55  Bible says count the cost. Count the cost before you start. There's
01:33:01  something powerful in consecration and saying, "Lord, I will do whatever you
01:33:08  ask me to do." >> Thank you, Lord. >> Amen. >> Thank you, Jesus. >> Would
01:33:13  that qualify to anybody here today? >> Thank you, Jesus. Thank you, Jesus.
01:33:18  >> Thank you, Jesus. >> Come, come forward >> if you would if that applies
01:33:22  to you here today.
01:33:27  >> Thank you, Lord. >> Thank you, Jesus. Thank you, Lord. >> Thank you, Lord.
01:33:31  >> Thank you, Lord. >> It requires boldness to step out to answer that
01:33:38  question truthfully. >> Thank you, Lord. >> Because it means that you're not willing
01:33:41  to sit there any longer. >> Thank you, Jesus. >> Amen. >> Amen. And L,
01:33:46  I want to say something before we pray. We're anointed to do
01:33:49  this, by the way. The spirit of the Lord is upon us.
01:33:53  We're anointed. This ministry is anointed. You know what this ministry is anointed
01:33:57  to do? exactly what he just said. Move people from where they
01:34:01  are to where God's called them to be. That's the word he
01:34:04  spoke over this church. So as we lay hands on you, that
01:34:07  anointing is on you. You're a part of this church. Father, in
01:34:11  the name. Go ahead and pray, John. >> Amen. >> In the name. >> So
01:34:15  tonight, the Lord asks you that question. >> Will you choose me? Will
01:34:22  you choose the plan that I have for you? Will you step
01:34:25  out beyond where you've been? because there's a place for you. >> Thank
01:34:30  you. >> There's a place beyond [music] where you've been that he wants
01:34:34  for you. So say yes. >> Say yes tonight. And he will cause
01:34:40  you to grow. He will cause you to go beyond where you've
01:34:44  been. >> And you will go further than you ever imagined. >> The Bible
01:34:50  says that we do not know the plans that he has for
01:34:53  us. the the fullness, the wonders, the the the greatness of it
01:34:57  because it it requires us to step out >> to step out to
01:35:02  see it one step at a time. So I believe tonight there
01:35:06  is an anointing on you that there is a grace on you
01:35:11  >> to step out and go beyond where you've been before in Jesus
01:35:15  name. >> In the name of Jesus. >> Amen. >> Amen. Amen. Thank you Lord.
01:35:19  Praise you father. Thank you Lord. Praise you, Father. Kaylee, can we
01:35:24  pray for you? Thank you, Lord. Thank you, Lord. I just felt
01:35:30  impressed. Is it okay if we just do this, guys? Is it
01:35:33  okay if we just just are led by the spirit for just
01:35:35  a moment? It's okay if you say, "No, I'm going to do it
01:35:37  anyway." So, praise God. I just Good practice. I don't know. The
01:35:41  Lord just want me to pray over you. Thank you, Lord. Father,
01:35:47  in the name of Jesus. Oh, this is what I hear the
01:35:52  Lord saying right now. The spirit of the Lord is upon you
01:35:56  because he's anointed you. He's anointed you in ways that you haven't
01:36:03  thought you were. He's anointed you in aspects in in uh abilities
01:36:12  that that you thought weren't in you that you thought you didn't
01:36:17  have. But the Lord is saying, "Hey, I put those things there."
01:36:21  And those things that you've seen in your heart already that you've
01:36:26  seen yourself doing and you thought, "Oh, no. I'm no that." No,
01:36:31  no. Those things that you've seen you doing and And I sure
01:36:35  hear the Lord saying this too. Your family doing your family doing.
01:36:40  This is not just a Kaye thing. This is a family thing.
01:36:44  Thank you, Lord. Oh, he's working in your family right now in
01:36:49  the name of Jesus. Thank you, Lord. This is a family anointing.
01:36:53  The family will be ministering together. The family will Thank you, Lord.
01:37:02  We pray over their entire Let's pray over their whole family. Your
01:37:06  whole family right now in the name of Jesus. Oh, for Kevin,
01:37:10  for cash. Thank you, Lord, for Thank you, Lord. Oh, yes. Thank
01:37:15  you, Jesus. In the name of Jesus. We thank you, Lord, over
01:37:20  every one of them. Thank you, Lord, for Colby. In the name
01:37:24  of Jesus, the anointing is on her as well. Thank you, Jesus.
01:37:30  Thank you, Father. Thank you, Lord. To do what you've called them
01:37:34  to do.
01:37:37  Oh, it's a season right now that you're in, but the Lord
01:37:40  says seasons change. Seasons change. You're not going to be in this
01:37:45  season forever. Seasons change. He's already working. He's already moving. And you
01:37:51  don't you don't you're not going to see it all in the
01:37:53  natural. You're not going to see things change overnight, just [music] like
01:37:56  the changing of seasons don't just change overnight. But gradually, you'll see
01:38:01  the season beginning to change. Just like in the spring, you start
01:38:04  to see flowers starting to bloom, trees starting to bloom, and you'll
01:38:09  be like, "Wow, it's a little cool outside, but look at that.
01:38:12  Look at that. Things [music] are beginning to change. You'll see the
01:38:16  same thing in your family. You'll begin to see the same thing.
01:38:21  Oh, thank you, Lord. Things are changing. The anointing The anointing is
01:38:27  on. The anointing is on your family because God doesn't just call
01:38:31  individuals, he calls families. Thank you, Lord, for that anointing on our
01:38:36  life in the name of Jesus. Praise you, Father. Thank you, Lord.
01:38:41  Let's give the Lord a hand for that one. Thank you, Jesus.
01:38:44  Thank you, Father. Thank you, Lord. We serve a good God. Amen.
01:38:50  Thank you, Lord.
01:38:54  Let's just pray for a minute. Thank you Lord. Thank you Jesus.
01:39:00  >> Thank you Lord. >> Thank you Jesus. >> Thank you Lord. To say that
01:39:07  I had dental work done today and it's been hurting pretty much
01:39:10  ever since. [music] And then when we were praying even coming up
01:39:13  here it just kept hurting and kept hurting and just in the
01:39:15  midst of praying he's [music] completely gone. So I don't have any
01:39:19  more pain. So I'm very thankful for that. So >> thank you >> just
01:39:23  being in the anointing. >> Amen. See, you can minister under the anointing
01:39:28  when you're having physical pain yourself. Well, that's a good word for
01:39:32  somebody. That's a good word for somebody. Some of y'all disqualified yourself
01:39:37  because of your condition. Or you said, "No, I experienced this and
01:39:41  I have this problem, so I can't minister to nobody." That's a
01:39:44  lie from the pit of hell. That same anointing in you will
01:39:48  heal your body and flow into somebody else and heal their body.
01:39:52  Thank you, Jesus, for it. Thank you, Lord, for healing teeth, toothaches
01:39:57  in the name of Jesus. Thank you, Lord. Thank you, Lord. Oh,
01:40:02  you're such a good father. You're such a good father. Thank you,
01:40:07  Jesus.
01:40:11  Thank you, Lord. >> Thank you, Lord. Thank you, Jesus.
01:40:22  Chains broken [singing and music] hearts open you
01:40:29  [singing] are healed in Jesus name. >> Chains
01:40:37  be [singing and music] broken hearts be open. You [singing] are
01:40:44  healed in Jesus name. Chains be
01:40:52  broken, [singing] hearts [music] be open. You are healed
01:40:59  in Jesus [singing] name. Hearts be [singing]
01:41:07  eyes be.
01:41:13  >> Thank you Jesus name. [singing] >> Thank you Lord. I want everybody to
01:41:18  say this with me. The spirit of the Lord >> The Spirit of
01:41:22  the Lord >> is upon me. >> is upon me. >> You've anointed me. >> You've
01:41:26  anointed me >> to preach the gospel >> preach the gospel >> to the poor.
01:41:32  >> You've anointed me >> You've anointed me >> to lay hands >> to lay hands
01:41:36  >> on blind eyes >> on blind eyes. >> You've anointed me >> You've anointed me
01:41:41  >> to cast out demons >> to cast out [music] demons >> in the name
01:41:45  >> In the name >> of Jesus. of Jesus, >> the anointed one. >> The anointed
01:41:49  one >> with his anointing >> with his anointing. >> Thank you, Lord. Thank you,
01:41:53  Father. >> Oh, thank you, Lord. >> Thank you, Jesus. >> I just hear the
01:41:58  Lord saying this, too.
01:42:03  You need to know who you are.
01:42:07  If you only knew who you were and whose you were, renew
01:42:12  your mind to it.
01:42:16  Who do you belong to? Who's anointed you? That should drive out
01:42:21  all fear of failure. Drive out all fear of stepping out in
01:42:26  faith. God, his anointing is on your life. Use
01:42:33  it. Use it. You're anointed to go to work tomorrow. Praise you,
01:42:39  Father. Don't Don't dread it. You're anointed to do it. You're anointed
01:42:43  to fix problems nobody [music] else can fix. You're anointed to have
01:42:47  ideas out of your spirit that nobody's thought about. We got [music]
01:42:51  a problem. We need a new idea. The anointing will bring you
01:42:54  an idea. Thank you, Lord. I heard the Lord saying this. The
01:43:00  church has not operated in this anointing as they should. And this
01:43:04  is just a little sample tonight. You can operate under this anointing
01:43:07  all the time. The anointing is not just for healing. The supernatural
01:43:12  power, this anointing that's on your life is to do to do
01:43:17  what? Whatever is needed. It's kind of like spiritual gifts. They say, "Which
01:43:22  one's the best spiritual gift?" It's the one that's needed at the
01:43:24  time. You're anointed to do that one. God's anointed you for such
01:43:30  a time as this. Amen. I want to pray over everybody before
01:43:33  we go. Father, in the name of Jesus, I thank you for
01:43:37  this church. Oh, it's an anointed church. Powerful church. Thank you, Lord,
01:43:44  for the anointing on every single person's life here tonight. I thank
01:43:49  you, Lord, that we tonight are coming up to a new level,
01:43:54  functioning in, operating with, cooperating with you in that anointing. And that
01:44:01  everything that we do in this life from this point forward, everything
01:44:05  that we are challenged with, every time that we feel like we're
01:44:09  not enough, we feel like we can't, that's when we connect with
01:44:13  that anointing. That's when the anointing takes over and we say, "I
01:44:17  can do all things. Not in my own strength, not in my
01:44:22  own ability, but through Christ and his anointing. The anointed one and
01:44:27  his anointing on my life is enabling me to go do all
01:44:32  that you've called me to do to be the Christian you've called
01:44:35  me to be in the name of Jesus. We thank you for
01:44:38  it. We praise you for it in Jesus name. Praise you, Father.
01:44:43  I don't like to close services like this. I just like to
01:44:47  keep going. Amen. Praise God. Thank you, Lord. Isn't God good? Amen.
01:44:52  He's a good father. Invite someone to church this Sunday. I know
01:44:55  it's Mother's Day. You have something else to say, >> Miss Francis Marie.
01:44:59  You know, tomorrow is her birthday. She has to come here. [laughter]
01:45:03  >> If I know it's your birthday, you better watch out. >> Let's have
01:45:06  an anointed song, shall we? >> We love her. She's been a part
01:45:10  of our church for many [music] years and a huge blessing. And
01:45:12  we love you and we just want to honor you. So, we're
01:45:15  gonna sing happy birthday. >> Here we go. Happy birthday [singing] to you.
01:45:22  Happy birthday to you. >> Happy birthday, Princess Marie.
01:45:31  [laughter] >> Happy birthday to you.
01:45:37  >> All right. Thank you guys. You guys are dismissed. God bless y'all.
```

### 5c. Transcript excerpt — prophetic/ministry language matches

_keyword regex: prophesy/prophetic, word from the Lord, healing, lay hands, tongues, fire, presence, altar, come forward, receive, impartation, deliverance_

```
00:04:55  welcome to Movement Church. [music] Miracle and healing night. Are you excited?
00:23:38  May I never lose the wonder of your [singing] presence. [music] May
00:25:58  [music] [singing] your presence I always stand of who you
00:26:09  of the beauty and the [music] gift of [singing] your presence
00:27:05  his presence. Oh, we turn our attention to you, Jesus. [music] May
00:29:27  You know, there's just nothing like being in the presence of God.
00:30:06  in God's presence and stay the way you are. Can you imagine
00:32:41  Healing and miracle night at Movement Church. We got any hungry people
00:33:03  we're going to pray for some people, lay hands on some people.
00:33:15  a lot Thank you. a lot of things to do with healing.
00:35:12  and now they're healed. Somebody was missing something in their life and
00:35:19  When the manifested power and presence of God shows up, it changes
00:35:41  to lay hands on people. I don't want to do anything. It's
00:36:01  I I want to share a little bit about how we receive
00:36:05  this healing and when we can have it. 2 Corinthians chapter 5:E1
00:38:41  in your spirit, soul, and body. Restored to health. Let me just
00:38:47  read it to you. The definition here. Restored to health to deliver,
00:38:52  to rescue you from danger, to make you whole, and to heal
00:38:56  you. So, it's really not a question whether or not healing is
00:39:06  healing is for today. I don't know if healing is a part of
00:39:22  concordance says that salvation so includes healing. So it's not really a
00:39:32  will question whether healing is for you. The question is where is
00:39:38  that healing? Where do I find that healing? Yeah, God heals people
00:39:47  and they'll say, "Yeah, healing is available and one day we'll be
00:39:49  healed when we get to heaven." Let me tell you something that
00:40:04  okay? When people approached Jesus and they needed healing in their body,
00:40:13  and then they're a leopard and say, "I know you can heal
00:40:23  to heaven and you'll be healed. Oh, you need healing in your
00:40:36  and then you'll be healed. But that's exactly what many people believe.
00:40:43  Many people believe that you'll get healed when you're in heaven. Let
00:40:46  me tell you tonight, there's nothing to be healed from in heaven.
00:40:51  There's nothing to be healed from. There's no sickness there. Of course,
00:40:54  there's no You're healed in heaven because there's no sickness in heaven
00:40:58  to be healed from. When when you leave your body one day,
00:41:11  STAYS HERE. YOUR BODY MUST not have gotten healed if it was
00:41:14  a sickness or disease that took you out. Well, they're healed in
00:41:17  heaven, but their body's still here and their body didn't get healed.
00:41:24  salvation includes healing. And you don't have to wait till you get
00:41:32  healing is available today. Amen. >> So, where does this healing come from?
00:41:38  How how is it that we have healing on this earth today?
00:41:57  me to heal the brokenhearted, to proclaim liberty to the captives and
00:42:27  healed because he was Jesus. Well, he was Jesus, so he could
00:42:30  heal people. No, he couldn't. He couldn't heal anybody until he was
00:42:54  anointed me to heal the brokenhearted, set at liberty though the to
00:43:02  do this. I am anointed to do this. How is healing happening
00:43:06  now on the earth? Because there's an anointed man going around healing
00:43:10  everybody. There's a man who's been anointed by the Holy Spirit healing
00:43:16  everybody. And everywhere he went, he's healing people. And he wasn't healing
00:43:27  he could heal them. That's another one people say, "Well, you know,
00:44:17  anointed to hurt you. He was anointed to heal you. And that
00:45:24  get from Jesus mouth himself how this healing is going to take
00:45:32  chapter 1 verse8 he said but you shall receive power when the
00:46:27  like fire coming from heaven and the fire came down on each
00:46:34  They began to speak with other tongues. You lose a lot of
00:46:57  Jesus did. He wants you walking around healing people. He wants you
00:47:02  walking around laying hands on people. Is that not what he told
00:47:38  ones that are to take healing and deliverance and open blind eyes
00:48:27  you and smacks you down because and sometimes Jesus will heal you
00:49:36  would put them on people and those people would be healed. Demons
00:53:06  on us. This is how people get healed today. It's because of
00:54:46  your life. So many Christians will get healed first before they even
00:56:22  People have over complicated this healing thing so bad and they try
00:59:59  anointing. You and I are anointed. How How is this healing going
01:00:49  cancer. The same power that heals sickness and disease. The same power
01:01:00  something. God wants every person here tonight healed. How do I know
01:01:19  means healing. And it starts now. I said it starts now. It
01:01:28  you to come forward right now. If you got pain in your
01:02:59  you, Lord, as the healer. And that anointing right now is flowing
01:03:04  into her body, healing what's been broken, uh, putting together, what's been
01:03:31  apply to you. Thank you, Lord, for healing right now in the
01:03:55  over her right now. Healing, wholeness over her lungs, clear lungs in
01:04:09  is upon us. We are anointed for this purpose to lay hands
01:05:42  receive all. I said all. I said all of the anointing that's
01:05:46  needed to heal every aspect, every every symptom in the name of
01:06:41  be saying things about us. How she's been healed, how she's been
01:06:45  delivered, how she no longer deals with those things any longer because
01:06:50  by Jesus stripes, she was healed. Thank you, Lord, for it. Thank
01:07:04  coming in. Oh, it's healing everything. Everything that's out of alignment in
01:07:13  being healed right now in the name of Jesus.
01:07:56  Well, you know, there was a time when Jesus healed people that
01:08:04  a centurion servant. He said, "I'll come heal your servant." And what
01:08:33  Lord, that right now that healing power is going into his body,
01:08:54  We speak to that mouth right now in Jesus name. Be healed
01:09:20  Thank you, Lord. He's healed by Jesus stripes. >> Thank you, Lord. >> Thank
01:09:34  else I heard the Lord say. You know, everybody that Jesus healed
01:10:09  name of Jesus, as we lay hands on her, we do exactly
01:10:38  Lord, that that anointing is flowing in her body right now. Healing
01:12:04  Let's pray for you. Okay, we lay hands on you and pray
01:12:22  Thank you Lord for that healing power. Thank you Lord for removing
01:13:39  said that Josh could come forward tonight and call on prayer. The
01:14:25  of Jesus. >> Restoration, wholeness, >> healing in the name.
01:14:58  minute. Thank you, Lord. Thank you, Lord. Jesus, for being our healer.
01:15:04  Thank you, Lord. Pastor Chris is not the healer. Jesus is the
01:15:08  healer. But Jesus has anointed us. He's empowered us to lay hands
01:16:38  here and we're just going to lay hands on your leg. And
01:16:41  when we lay hands on your leg, the power of God is
01:17:46  Thank you, Lord. That anointing right now is healing his tummy in
01:17:54  of Jesus. That anointing right now is healing his stomach. Stomach ache,
01:18:27  Jada was having some health issues. Jamie and Jasmine's little girl's having
01:18:31  some health issues this morning. And so she had to go uh
01:21:09  is upon us. You have anointed us. to do this to heal
01:23:37  want to lay hands on you and pray for you. Thank you,
01:27:03  depression. >> You're suffering from depression tonight. I want you to come forward
01:27:20  term, but you've been suffering from depression. The Lord says healing [music]
01:27:24  night is not just for physical things. Healing not is for everything
01:30:11  com uncomfortable for us to just worship in his presence. I think
01:30:18  do this or do that. But just spending time in his presence
01:31:47  healed?" >> Do you want to be healed? And it it's simple in
01:32:07  to be healed? Do you want to follow me for the rest
01:33:18  >> Thank you, Jesus. >> Come, come forward >> if you would if that applies
01:34:04  spoke over this church. So as we lay hands on you, that
01:39:48  heal your body and flow into somebody else and heal their body.
01:39:52  Thank you, Jesus, for it. Thank you, Lord, for healing teeth, toothaches
01:40:29  [singing] are healed in Jesus name. >> Chains
01:40:44  healed in Jesus name. Chains be
01:40:52  broken, [singing] hearts [music] be open. You are healed
01:41:32  >> You've anointed me >> You've anointed me >> to lay hands >> to lay hands
01:43:07  all the time. The anointing is not just for healing. The supernatural
```


---

## Consumed Church (N. Richland Hills, TX) — Pastor Jon Pignatelli — Margin — July 20,2026 (zaQ4mUHUBdA)

### 1. Manifest
```json
{
  "church": "Consumed Church (N. Richland Hills, TX)",
  "video_id": "zaQ4mUHUBdA",
  "url": "https://www.youtube.com/watch?v=zaQ4mUHUBdA",
  "title": "Pastor Jon Pignatelli \u2014 Margin \u2014 July 20,2026",
  "upload_date": "20260720",
  "duration_seconds": 7238,
  "whisper_model_used": "none \u2014 YouTube 'en-orig' auto-captions (ASR) substituted; Whisper impossible (media download blocked in sandbox, see PIPELINE_REPORT.md)",
  "notes": "metadata via yt-dlp web_embedded client (datacenter IP bot-check workaround); livestream release 2026-07-19T14:56:47Z"
}
```

### 2. Segments
```json
{
  "segments": [
    {
      "start": "00:00:00",
      "end": "00:05:00",
      "label": "other",
      "confidence": "high",
      "note": "pre-service"
    },
    {
      "start": "00:05:00",
      "end": "00:47:30",
      "label": "worship",
      "confidence": "high",
      "note": "includes spontaneous adoration/prayer 44:20-47:05"
    },
    {
      "start": "00:47:30",
      "end": "00:52:30",
      "label": "other",
      "confidence": "medium",
      "note": "greeting time"
    },
    {
      "start": "00:52:30",
      "end": "00:59:00",
      "label": "announcements",
      "confidence": "high",
      "note": "QR giving, church center app, mission"
    },
    {
      "start": "00:59:00",
      "end": "01:01:30",
      "label": "prayer",
      "confidence": "medium",
      "note": "corporate prayer over church and pastors"
    },
    {
      "start": "01:01:30",
      "end": "01:56:00",
      "label": "message",
      "confidence": "high",
      "note": "Margin (sabbath, hurry, John Mark Comer refs)"
    },
    {
      "start": "01:56:00",
      "end": "02:00:38",
      "label": "prayer",
      "confidence": "medium",
      "note": "communion + sending prayer"
    }
  ],
  "worship_minutes": 42.5,
  "message_minutes": 54.5,
  "ministry_minutes": 0.0,
  "worship_to_total_ratio": 0.352
}
```

### 3. Speech density (worship + ministry buckets only; 5-min buckets, ASR word counts)
```
05:00–10:00 | 314 words
10:00–15:00 | 238 words
15:00–20:00 | 315 words
20:00–25:00 | 312 words
25:00–30:00 | 326 words
30:00–35:00 | 354 words
35:00–40:00 | 280 words
40:00–45:00 | 232 words
45:00–50:00 | 362 words
```

### 4. Contact sheets (timestamps in tiles are true video time)
```
grid_baseline_01.jpg
grid_baseline_02.jpg
grid_baseline_03.jpg
grid_baseline_04.jpg
grid_baseline_05.jpg
grid_baseline_06.jpg
grid_baseline_07.jpg
grid_baseline_08.jpg
grid_dense_worship_tail_01.jpg
grid_dense_worship_tail_02.jpg
grid_dense_worship_tail_03.jpg
grid_dense_worship_tail_04.jpg
grid_dense_worship_tail_05.jpg
grid_dense_worship_tail_06.jpg
```

### 5a. Transcript excerpt — final 10 min of worship

```
00:37:33  worthy is the lamb." One more time. Worthy,
00:37:41  worthy is the lamb.
00:37:46  Worthy, worthy is the lamb.
00:37:54  >> Sing. Worthy is the lamb and worthy is the lamb.
00:38:02  Come on, lift it up. See it on the throne.
00:38:11  We crown you now with many crowns.
00:38:18  You reign victorious
00:38:23  high and lifted up high and lifted up.
00:38:31  Jesus son of God. Jesus son of God.
00:38:40  The dwelling of heaven crucified.
00:38:48  Worthy, worthy. Worthy is the lamb.
00:38:58  Worthy, worthy is the lamb.
00:39:04  Sing it again. Worthy is the lamb. Worthy, worthy,
00:39:13  worthy is the lamb. Oh, let's sing it again. Worthy is the
00:39:19  lamb
00:39:22  and worthy is the lamb.
00:39:29  Seated on the throne.
00:39:36  We call you down.
00:39:43  You reign victorious
00:39:48  high. High and lifted up. Jesus.
00:39:57  Jesus. Son of God.
00:40:04  The darling of heaven who
00:40:12  worthy is the lamb.
00:40:15  Worthy is the lamb.
00:40:23  Worthy is the lamb.
00:40:28  Worthy. Worthy is the lamb.
00:40:37  Worthy is the lamb.
00:40:49  >> We give you glory, God.
00:40:55  >> Worthy of praise. >> We give you glory, God.
00:41:04  Honor and riches worth. >> There's none like you. There's none beside
00:41:12  you.
00:41:16  Oh, worthy is the lamb.
00:41:23  Oh, worthy is the lamb.
00:41:30  Oh, worthy is the Lamb.
00:41:37  Oh, worthy is the Lamb. I want to keep singing and tell
00:41:43  him, "Oh, worthy is the Lamb."
00:41:52  Worthy is the lamb.
00:41:59  Worthy is the lamb.
00:42:07  Worthy is the
00:42:11  We love you.
00:42:15  We love you.
00:42:18  Oh, we love you,
00:42:25  Jesus. We love you.
00:42:32  Oh, how we love you.
00:42:39  You are the one.
00:42:46  >> Our hearts to
00:42:53  Jesus we love. love you.
00:43:00  >> Oh, how we love you.
00:43:08  >> You are the one
00:43:15  I heart to adore.
00:43:28  We love you, God.
00:43:49  How
00:43:55  you love
00:44:06  how we love
00:44:12  how we
00:44:24  I was just in awe of his presence in this room. I
00:44:27  just feel the glory cloud just kind of swirling around. I mean,
00:44:33  if you're not sensing it, just lean into his presence. Just focus
00:44:38  on him.
00:44:41  And as we've committed oursel to build our life on you and
00:44:47  put oursel in that posture, it's you who are doing the building.
00:44:52  Father, we just submit to your your construction project in us to
00:44:57  heal us, to make us whole. Father, >> thank you for your building
00:45:03  project in each one of us. And as you work on each
00:45:07  one, Father, you're building us into a community. Father, those lights and
00:45:13  salts in the earth, Father, we glorify you in this place, Father.
00:45:18  All the titles that we've called you this morning, they're just loaded.
00:45:22  They're just loaded with meaning. >> And Father, we just acknowledge the King
00:45:27  in this place. We acknowledge the son of God.
00:45:34  >> The darling of heaven. >> We acknowledge the darling of heaven. >> That son
00:45:40  of God. Even the title is has kingship all loaded in there.
00:45:46  Father, we do crown you. We do crown you with our lives.
00:45:52  You have been crowned. And we crown you again and again and
00:45:56  again. and every crown that we would hope to receive, we throw
00:45:59  it at your feet, Father, as the elders are doing right in
00:46:02  this moment, Father. We lay every achievement in our life before you,
00:46:09  Lord, just as you have taken every wrong and every destruction. We
00:46:14  give you everything that we've done right, Father. It's all for you.
00:46:19  We humble ourselves before you and say, "It is all you. It
00:46:24  is all your grace this morning and we receive from you, Lord.
00:46:28  That completed work that's promised, we receive it right now. Thank you
00:46:34  for your rescue from darkness. But we know saving is something that's
00:46:40  happening right now. You are saving us >> and you will save these
00:46:46  bodies in the resurrection. But I thank you. I thank you for
00:46:50  right now in this moment, how you're moving and you're saving us.
00:46:55  Thank you, God, for your saving power that's in your name. You
00:46:59  are the one who saves. Thank you, God. Let's just receive that
00:47:05  saving power over us right now.
00:47:11  >> Thank you, God.
00:47:15  >> Bless you, Lord.
00:47:18  Jesus.
00:47:24  Oh, how
```

### 5b. Transcript excerpt — ministry time (entirety)

_(no transcript content in this window — see PIPELINE_REPORT.md)_

### 5c. Transcript excerpt — prophetic/ministry language matches

_keyword regex: prophesy/prophetic, word from the Lord, healing, lay hands, tongues, fire, presence, altar, come forward, receive, impartation, deliverance_

```
00:05:10  for heaven to meet earth. And heaven is where God's presence is.
00:06:38  Father, we just receive life this morning that comes from your throne.
00:06:43  We thank you for your dwelling presence with us. Not just in
00:06:53  the presence of the Lord in this in this place. We receive
00:07:26  let let's just enter into his presence as he fills this place
00:24:52  >> Lord. We say thank you for being here. Thank you for delivering
00:44:24  I was just in awe of his presence in this room. I
00:44:33  if you're not sensing it, just lean into his presence. Just focus
00:44:57  heal us, to make us whole. Father, >> thank you for your building
00:45:56  again. and every crown that we would hope to receive, we throw
00:46:24  is all your grace this morning and we receive from you, Lord.
00:46:28  That completed work that's promised, we receive it right now. Thank you
00:46:59  are the one who saves. Thank you, God. Let's just receive that
00:54:02  Let's just read this together. As we receive today's offering, we call
00:58:44  that logistic work. Uh, when we deliver groceries this next Saturday, we'll
01:07:19  presence, and our attention.
01:21:39  he wasn't practicing the Sabbath. He would heal on the Sabbath. He
01:22:53  was high priest and ate the bread of the presence which only
01:23:48  Jesus would heal him on the Sabbath so that they could frame
01:24:40  We see here that the Sabbath is given to facilitate a healthy
01:31:21  free and the power and presence the spirit of God will be
01:35:56  all this effort to deliver you and to make you this special
01:40:05  I can't believe how delivered I am from that these days. You
01:49:02  in his presence with his people in community working for his purposes.
```


---

## Consumed Church (N. Richland Hills, TX) — Pastor Jon Pignatelli - Wrath, Love’s Fierce Opposition to Evil -  July 12, 2026 (UR1Jwm4gC4E)

### 1. Manifest
```json
{
  "church": "Consumed Church (N. Richland Hills, TX)",
  "video_id": "UR1Jwm4gC4E",
  "url": "https://www.youtube.com/watch?v=UR1Jwm4gC4E",
  "title": "Pastor Jon Pignatelli - Wrath, Love\u2019s Fierce Opposition to Evil -  July 12, 2026",
  "upload_date": "20260713",
  "duration_seconds": 7648,
  "whisper_model_used": "none \u2014 YouTube 'en-orig' auto-captions (ASR) substituted; Whisper impossible (media download blocked in sandbox, see PIPELINE_REPORT.md)",
  "notes": "WARNING: ASR captions absent for 00:00-00:52 (worship span) \u2014 speech density unreliable there; frames confirm live worship. metadata via yt-dlp web_embedded client (datacenter IP bot-check workaround); livestream release 2026-07-12T14:56:29Z"
}
```

### 2. Segments
```json
{
  "segments": [
    {
      "start": "00:00:00",
      "end": "00:04:00",
      "label": "other",
      "confidence": "high",
      "note": "title/give/connect slides"
    },
    {
      "start": "00:04:00",
      "end": "00:48:00",
      "label": "worship",
      "confidence": "medium",
      "note": "NO ASR captions for this span; storyboard frames show worship band throughout"
    },
    {
      "start": "00:48:00",
      "end": "00:53:00",
      "label": "announcements",
      "confidence": "medium",
      "note": "giving slides, testimony/greeting"
    },
    {
      "start": "00:53:00",
      "end": "00:56:00",
      "label": "prayer",
      "confidence": "medium"
    },
    {
      "start": "00:56:00",
      "end": "02:02:00",
      "label": "message",
      "confidence": "high",
      "note": "Wrath - Love's Fierce Opposition to Evil"
    },
    {
      "start": "02:02:00",
      "end": "02:07:28",
      "label": "prayer",
      "confidence": "medium",
      "note": "communion / response moment"
    }
  ],
  "worship_minutes": 44.0,
  "message_minutes": 66.0,
  "ministry_minutes": 0.0,
  "worship_to_total_ratio": 0.345
}
```

### 3. Speech density (worship + ministry buckets only; 5-min buckets, ASR word counts)
```
00:00–05:00 | 0 words
05:00–10:00 | 0 words
10:00–15:00 | 0 words
15:00–20:00 | 0 words
20:00–25:00 | 0 words
25:00–30:00 | 0 words
30:00–35:00 | 0 words
35:00–40:00 | 0 words
40:00–45:00 | 0 words
45:00–50:00 | 0 words
```

### 4. Contact sheets (timestamps in tiles are true video time)
```
grid_baseline_01.jpg
grid_baseline_02.jpg
grid_baseline_03.jpg
grid_baseline_04.jpg
grid_baseline_05.jpg
grid_baseline_06.jpg
grid_baseline_07.jpg
grid_baseline_08.jpg
grid_dense_worship_tail_01.jpg
grid_dense_worship_tail_02.jpg
grid_dense_worship_tail_03.jpg
grid_dense_worship_tail_04.jpg
grid_dense_worship_tail_05.jpg
grid_dense_worship_tail_06.jpg
```

### 5a. Transcript excerpt — final 10 min of worship

_(no transcript content in this window — see PIPELINE_REPORT.md)_

### 5b. Transcript excerpt — ministry time (entirety)

_(no transcript content in this window — see PIPELINE_REPORT.md)_

### 5c. Transcript excerpt — prophetic/ministry language matches

_keyword regex: prophesy/prophetic, word from the Lord, healing, lay hands, tongues, fire, presence, altar, come forward, receive, impartation, deliverance_

```
00:54:07  to be in your presence, Lord, to taste of of your spirit
00:54:48  have loved me back to health, for investing in my life, for
00:58:04  transfusion and a much healthier understanding of the cross? a much
00:58:11  healthier understanding, biblical understanding, uh, Jewishbased perspective on
00:58:25  it heals us, how it cleanses us. Um, now I had made
01:02:50  of us becoming an emotionally healthy church. Because part of our transformation
01:04:57  through the catch the fire network of being the co kid. It
01:05:07  fire leaders are known for their revival meetings. Uh you know, one
01:06:48  of talking about the secret that they were all getting healed of
01:07:20  bottle. Only takes a few drops to heal you of COVID. And
01:08:09  glamorous and um they they uh the catch the fire network people
01:09:08  God. We think of fire and brimstone. We think of God's hand
01:14:45  delivered from the Egyptians out of slavery and they walk through the
01:16:31  earrings and stuff off and he threw it in the fire and
01:16:38  >> Just rolled right out of just jumped right out of the fire
01:19:44  to deliver me. I don't even I don't even know what you
01:28:43  look like fire and brimstone or lightning bolts, but it's actually God
01:29:29  alive. So most of when you're reading the prophets in the Old
01:29:41  Jeremiah, it's this it's this constant plea through the prophet to the
01:31:00  doesn't describe wrath primarily as fire. He describes it as disintegration.
01:36:20  ways, then I will absolutely embrace them and heal them and bless
01:39:02  and healed me in so many ways. But I had to discover
01:39:54  tell you right now, you you can totally be delivered to that.
01:45:20  And that is a really really healthy approach for us to understand.
01:52:04  and health and unity that cannot be broken. That's why
01:54:41  Turn from the idols that are destroying you. Receive the God who
02:02:09  just a prophetic enactment, a tactile way for us to
02:04:55  is for you to heal you, to cleanse you, to purify you,
```


---

## Bonus: movement-church-celina/dCWJhrpKUrc (Jul 20 service)

Frames-only entry: no captions exist for this video, so no transcript/segments/density.
Baseline grids grid_baseline_01..07.jpg provided as visual evidence only.


See PIPELINE_REPORT.md for failures, fallbacks, and reliability caveats.
