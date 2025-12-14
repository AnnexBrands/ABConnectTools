# Compatability

## sj_misc.git

### save photos
```py
abapi.docs.upload_item_photos(
                jobid=row["Job"],
                itemid=row["JobItemID"],
                files={k: v},
            )
```